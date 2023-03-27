import psycopg2
import requests
import time
import pandas as pd

conn = psycopg2.connect("host='localhost' port='15432' dbname='de' user='jovyan' password='jovyan'")

api_host = 'https://d5dg1j9kt695d30blp03.apigw.yandexcloud.net'
nickname = 'AlexanderZhukov'
api_key = '5f55e6c0-e9e5-4a9c-b313-63c01fc31460'
cohort = 12

generate_report_response = requests.post(
    f"{api_host}/generate_report",  # точка входа
    headers={
        "X-API-KEY": api_key,  # ключ API
        "X-Nickname": nickname,  # авторизационные данные
        "X-Cohort": str(cohort)  # авторизационные данные
    }
).json()
task_id = generate_report_response["task_id"]

time.sleep(60)

get_report_response = requests.get(
    f"{api_host}/get_report?task_id={task_id}",
    headers={
        "X-API-KEY": api_key,
        "X-Nickname": nickname,
        "X-Cohort": str(cohort)
    }
).json()

if get_report_response['status'] == 'SUCCESS':
    data_paths = get_report_response['data']['s3_path']
    for name, path in data_paths.items():
        df = pd.read_csv(path)
        df.to_csv(f"C:\\Users\\aszhu\DE\YP\DE\\3_sprint\\stage/{name}.csv")
