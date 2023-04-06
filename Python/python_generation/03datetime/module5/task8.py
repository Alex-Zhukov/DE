from datetime import datetime, timedelta


def choose_plural(amount: int, declensions: tuple) -> str:
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in (2, 3, 4) and amount % 100 not in (12, 13, 14):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'


def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


def get_string_for_print(dt):
    result = []
    hours, minutes = hours_minutes(dt)
    if dt.days != 0:
        result.append(choose_plural(dt.days, ("день", "дня", "дней")))
        if hours != 0:
            result.append(choose_plural(hours, ("час", "часа", "часов")))
    else:
        if hours != 0:
            result.append(choose_plural(hours, ("час", "часа", "часов")))
        if minutes != 0:
            result.append(choose_plural(minutes, ("минута", "минуты", "минут")))

    return " и ".join(result)


planning_date = datetime(2022, 11, 8, 12, 0)

pattern = "%d.%m.%Y %H:%M"
current_date = datetime.strptime(input(), pattern)

remaining = planning_date - current_date

if remaining <= timedelta(0):
    print("Курс уже вышел!")
else:
    print(f"До выхода курса осталось: {get_string_for_print(remaining)}")
