import calendar
from datetime import datetime

pattern = "%Y-%m-%d"
input_dt = datetime.strptime(input(), pattern)
print(calendar.day_name[input_dt.weekday()])