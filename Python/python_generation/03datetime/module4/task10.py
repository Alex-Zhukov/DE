from datetime import datetime, time, timedelta

pattern = "%H:%M"
start_dttm = datetime.strptime(input(), pattern)
end_dttm = datetime.strptime(input(), pattern)

lesson_len = timedelta(minutes=45)
break_len = timedelta(minutes=10)

current_dttm = start_dttm
while current_dttm + lesson_len <= end_dttm:
    print(f"{datetime.strftime(current_dttm, pattern)} - {datetime.strftime(current_dttm + lesson_len, pattern)}")
    current_dttm += lesson_len + break_len
