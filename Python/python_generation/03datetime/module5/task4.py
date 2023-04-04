from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
left_date = datetime.strptime(input(), pattern)
right_date = datetime.strptime(input(), pattern)

while (left_date.day + left_date.month) % 2 == 0:
    left_date += timedelta(days=1)

delta = timedelta(days=3)
result = []

while left_date <= right_date:
    if left_date.weekday() != 0 and (left_date.weekday() != 3):
        result.append(left_date)
    left_date += delta

for dt in result:
    print(datetime.strftime(dt, pattern))
