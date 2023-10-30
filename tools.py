from datetime import date, time


def dEven_to_date(dEven: int | str):
    dEven = str(dEven)
    year = dEven[:4]
    month = dEven[4:-2]
    day = dEven[-2:]
    return date(year, month, day)


def hEven_to_time(hEven: int | str):
    hEven = str(hEven)
    hour = hEven[:2]
    minute = hEven[2:-2]
    second = hEven[-2:]
    return time(hour, minute, second)