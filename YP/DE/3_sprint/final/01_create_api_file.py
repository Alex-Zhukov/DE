import datetime as dt
import requests
import time
import pandas as pd

from airflow.hooks.base_hook import BaseHook
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import TaskInstance

api_host = BaseHook.get_connection("create_files_api").host
business_dt = {'dt': '2022-05-06'}
nickname = 'AlexanderZhukov'
api_key = '5f55e6c0-e9e5-4a9c-b313-63c01fc31460'
cohort = 12

headers = {
    "X-API-KEY": api_key,
    "X-Nickname": nickname,
    "X-Cohort": str(cohort)
}


def create_files_request(**kwargs):
    generate_report_response = requests.post(
        f"https://{kwargs['url']}{kwargs['method']}",
        headers=kwargs['headers']
    ).json()
    task_id = generate_report_response["task_id"]
    kwargs['ti'].xcom_push(value=task_id, key='task_id')


def upload_from_s3(file_names, **kwargs):
    task_id = kwargs['ti'].xcom_pull(task_ids="generate_files", key='task_id')
    conn_s3 = BaseHook.get_connection("conn_s3")
    url = "https://storage.yandexcloud.net/s3-sprint3-static/lessons/"
    target_path = "/lessons/5. Реализация ETL в Airflow/4. Extract как подключиться к хранилищу, чтобы получить файл/Задание 2/"
    for file_name in file_names:
        df = pd.read_csv(url + file_name)
        df.to_csv(target_path + file_name)


args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 12, 23)
}

dag = DAG(
    dag_id='epicDag',
    schedule_interval=None,
    default_args=args
)

generate_files = PythonOperator(
    task_id='generate_files',
    python_callable=create_files_request,
    op_kwargs={'url': api_host, 'method': '/generate_report', 'headers': headers},
    dag=dag,
)

generation_wait = BashOperator(
    task_id="delay_bash_task",
    bash_command='sleep 2',
    dag=dag)

upload_to_local = PythonOperator(
    task_id="upload_from_s3",
    python_callable=upload_from_s3,
    op_kwargs={'file_names': ['customer_research.csv',
                              'user_activity_log.csv',
                              'user_order_log.csv']},
    provide_context=True,
    dag=dag
)

generate_files >> generation_wait >> upload_to_local
