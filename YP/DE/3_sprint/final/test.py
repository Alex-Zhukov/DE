import requests

api_host = 'https://d5dg1j9kt695d30blp03.apigw.yandexcloud.net'
nickname = 'AlexanderZhukov'
api_key = '5f55e6c0-e9e5-4a9c-b313-63c01fc31460'
cohort = 12

generate_report_response = requests.post(
    f"{api_host}/generate_report", # точка входа
    headers={
    "X-API-KEY": api_key, # ключ API
    "X-Nickname": nickname, # авторизационные данные
    "X-Cohort": str(cohort) # авторизационные данные
    }
).json()
task_id = generate_report_response["task_id"]
print(generate_report_response)
