import calendar

year, mon = map(int, input().split())
print(calendar.monthrange(year, mon)[1])