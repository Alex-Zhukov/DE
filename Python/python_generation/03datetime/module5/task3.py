from datetime import datetime, time

schedule = {}
for i in range(7):
    open_time = time(9, 0) if i < 5 else time(10, 0)
    close_time = time(21, 0) if i < 5 else time(18, 0)
    schedule[i] = {"open": open_time, "close": close_time}

pattern = "%d.%m.%Y %H:%M"

input_date = datetime.strptime(input(), pattern)
weekday = input_date.weekday()
combined_date = datetime.combine(datetime.now().date(), input_date.time())

time_to_open = (combined_date - datetime.combine(datetime.today(), schedule[weekday]['open'])).total_seconds()
time_to_close = (datetime.combine(datetime.today(), schedule[weekday]['close']) - combined_date).total_seconds()

if time_to_open > 0 and time_to_close > 0:
    print(int(time_to_close // 60))

else:
    print("Магазин не работает")


# from datetime import datetime, timedelta
#
# dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# td = timedelta(hours=dt.hour, minutes=dt.minute)
#
# if dt.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
#     print(int((timedelta(hours=21) - td).total_seconds() // 60))
# elif dt.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
#     print(int((timedelta(hours=18) - td).total_seconds() // 60))
# else:
#     print('Магазин не работает')