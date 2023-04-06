import calendar

year, mon = input().split()

idx = [idx for idx, month in enumerate(calendar.month_abbr) if month == mon][0]
calendar.prmonth(int(year), idx)


# from calendar import prmonth
# from datetime import datetime
#
# dt = datetime.strptime(input(), '%Y %b')
#
# prmonth(dt.year, dt.month)