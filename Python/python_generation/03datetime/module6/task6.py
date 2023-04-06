import calendar
from datetime import date


def get_days_in_month(year, month_name):
    month_int = list(calendar.month_name).index(month_name)
    max_day = calendar.monthrange(int(year), month_int)[1]
    return [date(year, month_int, day) for day in range(1, max_day + 1)]


print(get_days_in_month(2021, 'December'))
