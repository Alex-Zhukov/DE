from datetime import datetime


def get_days_diff(dates):
    if len(dates_list) <= 1:
        return []
    else:
        return [abs(dates[i - 1] - dates[i]).days for i in range(1, len(dates))]


dates_list = [datetime.strptime(i, "%d.%m.%Y") for i in input().split()]

print(get_days_diff(dates_list))
