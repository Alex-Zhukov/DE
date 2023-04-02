import time
import requests
import json
from datetime import datetime
import pandas as pd
import psycopg2

from airflow import DAG
from airflow.hooks.base_hook import BaseHook
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.hooks.http_hook import HttpHook

http_conn_id = HttpHook.get_connection('http_conn_id')
api_key = http_conn_id.extra_dejson.get('api_key')
base_url = http_conn_id.host

postgres_conn_id = 'postgresql_de'

nickname = 'ZhukovAlexander'
cohort = '12'

headers = {
    'X-Nickname': nickname,
    'X-Cohort': cohort,
    'X-Project': 'True',
    'X-API-KEY': api_key,
    'Content-Type': 'application/x-www-form-urlencoded'
}


def insert_into_db(df, insert_statement, conn):
    current = 0
    step = int(df.shape[0] / 100)
    cur = conn.cursor()
    while current < df.shape[0]:
        print(current)
        insert_str = str([tuple(x) for x in df.loc[step:step + step].to_numpy()])[1:-1]
        cur.execute(insert_statement.replace('{insert_statement}', insert_str))
        conn.commit()
        current += step + 1
    cur.close()


def generate_report(ti):
    print('Making request generate_report')

    response = requests.post(f'{base_url}/generate_report', headers=headers)
    response.raise_for_status()
    task_id = json.loads(response.content)['task_id']
    ti.xcom_push(key='task_id', value=task_id)
    print(f'Response is {response.content}')


def get_report(ti):
    print('Making request get_report')
    task_id = ti.xcom_pull(key='task_id')

    report_id = None

    for i in range(20):
        response = requests.get(f'{base_url}/get_report?task_id={task_id}', headers=headers)
        response.raise_for_status()
        print(f'Response is {response.content}')
        status = json.loads(response.content)['status']
        if status == 'SUCCESS':
            report_id = json.loads(response.content)['data']['report_id']
            break
        else:
            time.sleep(10)

    if not report_id:
        raise TimeoutError()

    ti.xcom_push(key='report_id', value=report_id)
    print(f'Report_id={report_id}')


def upload_from_s3_to_pg(ti):
    report_id = ti.xcom_pull(key='report_id')

    storage_url = 'https://storage.yandexcloud.net/s3-sprint3/cohort_{COHORT_NUMBER}/{NICKNAME}/project/{REPORT_ID}/{FILE_NAME}'

    personal_storage_url = storage_url.replace("{COHORT_NUMBER}", cohort)
    personal_storage_url = personal_storage_url.replace("{NICKNAME}", nickname)
    personal_storage_url = personal_storage_url.replace("{REPORT_ID}", report_id)

    psql_conn = BaseHook.get_connection('postgresql_de')
    conn = psycopg2.connect(
        f"dbname='de' port='{psql_conn.port}' user='{psql_conn.login}' host='{psql_conn.host}' password='{psql_conn.password}'")

    # customer_research
    customer_research = pd.read_csv(personal_storage_url.replace("{FILE_NAME}", "customer_research.csv"), index_col=0)
    insert_customer = "insert into stage.customer_research (date_id, category_id, geo_id, sales_qty, sales_amt) VALUES {insert_statement};"
    insert_into_db(customer_research, insert_customer, conn)

    # user_orders_log
    user_orders_log = pd.read_csv("stage/user_order_log.csv", index_col=0)
    user_orders_log.drop(columns=["uniq_id"], inplace=True)
    insert_uol = "insert into stage.user_order_log (id, date_time, city_id, city_name, customer_id, first_name, last_name, item_id, item_name, quantity, payment_amount) VALUES {insert_statement};"
    insert_into_db(user_orders_log, insert_uol, conn)

    # user_activity_log
    user_activity_log = pd.read_csv("stage/user_activity_log.csv", index_col=0)
    user_activity_log.drop(columns=["id", "uniq_id"], inplace=True)
    insert_ual = "insert into stage.user_activity_log (date_time, action_id, customer_id, quantity) VALUES {insert_statement};"
    insert_into_db(user_activity_log, insert_ual, conn)

    conn.close()


args = {
    "owner": "AlexanderZhukov",
    'retries': 0
}

business_dt = '{{ ds }}'

dag = DAG(
    dag_id='initialize',
    start_date=datetime.today(),
    schedule_interval=None,
    default_args=args
)

generate_report = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,
    dag=dag
)

get_report = PythonOperator(
    task_id='get_report',
    python_callable=get_report,
    dag=dag
)

create_stage_tables = PostgresOperator(
    task_id="create_stage_tables",
    postgres_conn_id="postgresql_de",
    sql="sql/stage_ddl.sql",
)

upload_from_s3_to_pg = PythonOperator(task_id='upload_from_s3',
                                      python_callable=upload_from_s3_to_pg,
                                      # op_kwargs={
                                      #     "headers": headers
                                      # },
                                      provide_context=True,
                                      dag=dag)

create_stage_tables >> generate_report >> get_report >> upload_from_s3_to_pg
