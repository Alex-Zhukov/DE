from datetime import time, timedelta

input_date = time.fromisoformat(input())
input_delta = timedelta(hours=input_date.hour, minutes=input_date.minute, seconds=input_date.second)

print(int(input_delta.total_seconds()))
