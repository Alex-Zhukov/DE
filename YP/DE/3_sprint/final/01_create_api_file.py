import datetime as dt
from airflow.hooks.base_hook import BaseHook
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import requests
import time

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
    return task_id


args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 12, 23)
}

dag = DAG(
    dag_id='epicDag',  # Имя DAG
    schedule_interval=None,  # Периодичность запуска, например, "00 15 * * *"
    default_args=args,  # Базовые аргументы
)

generate_files = PythonOperator(
    task_id='generate_files',
    python_callable=create_files_request,
    op_kwargs={'url': api_host, 'method': '/generate_report', 'headers': headers},
    dag=dag,
)

bash_10s = BashOperator(
    task_id="delay_bash_task",
    bash_command='sleep 10',
    dag=dag)

python_10s = PythonOperator(
    task_id="delay_python_task",
    python_callable=lambda _: time.sleep(10),
    dag=dag
)

generate_files >> bash_10s >> python_10s
