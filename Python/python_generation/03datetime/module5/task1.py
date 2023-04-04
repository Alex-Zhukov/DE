from datetime import datetime

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

pattern = "%H:%M"

time_spent_seconds = sum([(datetime.strptime(task[1], pattern) - datetime.strptime(task[0], pattern)).seconds
                          for task in data])

print(time_spent_seconds // 60)
