from datetime import datetime, timedelta

NUMBER_OF_TASKS = 10

current_date = datetime.strptime(input(), "%d.%m.%Y")

for i in range(2, NUMBER_OF_TASKS + 2):
    print(current_date.strftime("%d.%m.%Y"))
    current_date += timedelta(days=i)
