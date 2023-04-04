from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    dates_list = [datetime.strptime(i, "%d.%m.%Y") for i in dates]
    delta = timedelta(days=1)
    result = []
    current_date = min(dates_list)
    while current_date <= max(dates_list):
        result.append(current_date)
        current_date += delta
    return [datetime.strftime(i, "%d.%m.%Y") for i in result]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))


# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]