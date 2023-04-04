from datetime import datetime, timedelta

schedule = {
    0: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }

pattern = "%d.%m.%Y %H:%M"

input_date = datetime.strptime(input(), pattern)
