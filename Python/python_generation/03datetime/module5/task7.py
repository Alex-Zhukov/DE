from datetime import datetime, timedelta


pattern = "%d.%m.%Y"
day_month_pattern = "%d.%m"
seven_days = timedelta(days=7)

current_date = datetime.strptime(input(), pattern)
employees = [input().split() for _ in range(int(input()))]

print(current_date + seven_days)
print(datetime.strptime(employees[0][2], day_month_pattern))
# nearest_birhday_employees = [emp for emp in employees
#                              if current_date <= datetime.timedelta(days=<= current_date + seven_days ]
