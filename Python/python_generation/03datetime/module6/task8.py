import calendar
from datetime import datetime


def get_free_days(year):
    days = []
    for month in range(1, 13):
        mnth_cal = calendar.monthcalendar(year, month)
        if mnth_cal[0][3] != 0:
            day = mnth_cal[2][3]
        else:
            day = mnth_cal[3][3]
        days.append(datetime(year=year, month=month, day=day))
    return days


input_year = int(input())
result = [datetime.strftime(x, "%d.%m.%Y") for x in get_free_days(input_year)]
print(*result, sep="\n")
