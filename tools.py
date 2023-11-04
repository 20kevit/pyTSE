from datetime import date, time


def dEven_to_date(dEven: int | str):
    print(dEven)
    dEven = str(dEven)
    year = int(dEven[:4])
    month = int(dEven[4:-2])
    day = int(dEven[-2:])
    return date(year, month, day)


def hEven_to_time(hEven: int | str):
    hEven = str(hEven).zfill(6)
    hour = int(hEven[:2])
    minute = int(hEven[2:-2])
    second = int(hEven[-2:])
    return time(hour, minute, second)