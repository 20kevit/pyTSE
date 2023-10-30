from datetime import date

def dEven_to_date(dEven: int | str):
    dEven = str(dEven)
    year = dEven[:4]
    month = dEven[4:-2]
    day = dEven[-2:]
    return date(year, month, day)