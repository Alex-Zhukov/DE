from datetime import datetime, timedelta

pattern = "%d.%m.%Y"

employees = [input().split() for _ in range(int(input()))]

oldest = min(employees, key=lambda x: datetime.strptime(x[2], pattern))[2]

olders_employees = [emp for emp in employees if emp[2] == oldest]

if len(olders_employees) == 1:
    print(f"{oldest} {' '.join(olders_employees[0][:2])}")
else:
    print(f"{oldest} {len(olders_employees)}")
