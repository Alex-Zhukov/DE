import calendar
from datetime import date


def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            candidate = date(year=year, month=month, day=day)
            if candidate.weekday() == 0:
                mondays.append(candidate)
    return mondays


print(sorted(get_all_mondays(2021)))
