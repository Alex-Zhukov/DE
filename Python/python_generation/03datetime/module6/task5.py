import calendar

year, mon = input().split()
print(calendar.monthrange(int(year), list(calendar.month_name).index(mon))[1])
