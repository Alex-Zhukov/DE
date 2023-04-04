from datetime import datetime, timedelta


pattern = "%d.%m.%Y"
day_month_pattern = "%d.%m"
seven_days = timedelta(days=7)

current_date = datetime.strptime(input(), day_month_pattern)
employees = [input().split() for _ in range(int(input()))]

nearest_birhday_employees = [emp for emp in employees
                             if datetime.strptime(emp[2], day_month_pattern) + seven_days ]
