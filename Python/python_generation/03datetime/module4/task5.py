from datetime import datetime, time, timedelta

input_date = datetime.strptime(input(), "%H:%M:%S")
n = int(input())
print((input_date + timedelta(seconds=n)).time())

