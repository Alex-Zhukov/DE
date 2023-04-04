from datetime import date, timedelta

results = {}
start_date = date(1, 1, 13)
end_date = date(9999, 12, 13)

day = timedelta(days=1)

cur_date = start_date
while cur_date <= end_date:
    if cur_date.day == 13:
        results[cur_date.weekday()] = results.get(cur_date.weekday(), 0) + 1
    cur_date += day

for k, v in sorted(results.items(), key=lambda x: x[0]):
    print(v)
