from datetime import date, timedelta

def num_of_sundays(year):
    sundays = 0
    start_dt = date(year, 1, 1)
    current_dt = date(year, 1, 1)
    delta = timedelta(days=1)
    while start_dt.year == current_dt.year:
        if current_dt.weekday() == 6:
            sundays += 1
        current_dt += delta
    return sundays


print(num_of_sundays(2021))
year = 2000
print(num_of_sundays(year))
print(num_of_sundays(768))
