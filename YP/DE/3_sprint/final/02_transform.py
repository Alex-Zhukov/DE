from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.hooks.base import BaseHook
from airflow.operators.python import PythonOperator

import datetime
import requests
import pandas as pd
import os
import psycopg2, psycopg2.extras

dag = DAG(
    dag_id='552_postgresql_export_fuction',
    schedule_interval='0 0 * * *',
    start_date=datetime.datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['example', 'example2'],
    params={"example_key": "example_value"},
)
business_dt = {'dt':'2022-05-06'}

conn_args = BaseHook.get_connection("pg_connection")


def load_file_to_pg(file_name, pg_table, conn_args):

    df = pd.read_csv(f"/lessons/5. Реализация ETL в Airflow/4. Extract как подключиться к хранилищу, чтобы получить файл/Задание 2/{file_name}", index_col=0)


    cols = ','.join(list(df.columns))
    insert_stmt = f"INSERT INTO stage.{pg_table} ({cols}) VALUES %s"


    pg_conn = psycopg2.connect(conn_args.get_uri())
    cur = pg_conn.cursor()

    psycopg2.extras.execute_values(cur, insert_stmt, df.values)
    pg_conn.commit()

    cur.close()
    pg_conn.close()

load_to_pg = PythonOperator(
    task_id='load_file_to_pg',
    python_callable=create_files_request,
    op_kwargs={'url': api_host, 'method': '/generate_report', 'headers': headers},
    dag=dag,
)

load_to_pg