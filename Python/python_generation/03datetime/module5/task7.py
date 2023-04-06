from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
day_month_pattern = "%d.%m"
seven_days = timedelta(days=7)

current_date = datetime.strptime(input(), pattern)
employees = [input().split() for _ in range(int(input()))]

nearest_birhday_employees = []
for emp in employees:
    emp_name = " ".join(emp[:2])
    emp_bd = datetime.strptime(emp[2], pattern)
    combined_dt = datetime(current_date.year, emp_bd.month, emp_bd.day)
    if emp_bd.month == 1 and emp_bd.day <= 7:
        combined_dt = datetime(current_date.year + 1, emp_bd.month, emp_bd.day)
    if current_date < combined_dt <= current_date + seven_days:
        nearest_birhday_employees.append((emp_name, emp_bd))

print(max(nearest_birhday_employees, key=lambda x: x[1])[0]
      if nearest_birhday_employees else "Дни рождения не планируются")
