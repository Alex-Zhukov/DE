from datetime import datetime, timedelta

pattern = "%d.%m.%Y"

employees = [input().split() for _ in range(int(input()))]

dates_dict = {}

for emp in employees:
    dates_dict[emp[2]] = dates_dict.get(emp[2], 0) + 1

max_count = max(dates_dict.values())

result = [datetime.strptime(k, pattern) for k, v in dates_dict.items() if v == max_count]

for dt in sorted(result):
    print(datetime.strftime(dt, pattern))
