import requests
import pandas as pd
import URLs
from datetime import datetime

USER_AGENT = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"


def get(url):
    return requests.get(
        url=url,
        headers={"User-Agent": USER_AGENT}
    )


def search(search_key: str) -> list:
    """first item is the best match"""
    url = URLs.SEARCH.format(key=search_key)
    response = get(url)
    if not response.text:
        return list()
    results = response.text.split(";")[:-1]
    data = pd.DataFrame([result.split(',')[:3] for result in results])
    data.columns = ["symbol", "name", "insCode"]
    return data


def history(insCode: int | str, days: int = 0) -> pd.DataFrame:
    days = 0 if days < 0 else days
    url = URLs.CLOSING_PRICE_DAILY_LIST.format(
        insCode=insCode,
        n=days
    )
    response = get(url).json()["closingPriceDaily"]
    if not response:
        return pd.DataFrame()
    data = pd.DataFrame(response)
    data.drop(
        columns=["last", "id", "insCode", "hEven",
                 "iClose", "yClose", "priceChange"],
        inplace=True
    )
    data.rename(
        columns={
            "priceMin": "low",
            "priceMax": "high",
            "priceYesterday": "yesterday",
            "priceFirst": "first",
            "dEven": "date",
            "pClosing": "close",
            "pDrCotVal": "last",
            "zTotTran": "number",  # number of transactions
            "qTotTran5J": "volume",  # volume of transactions
            "qTotCap": "value"  # value of transactions
        },
        inplace=True
    )
    data.set_index('date', inplace=True)
    data = data.astype(dtype='int64')

    return data


def instrument_info(insCode: int | str):
    url = URLs.TICKER_INSTRUMENT_INFO.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["instrumentInfo"]
    return {
        "date": data["dEven"],
        "daily_threshold": (
            int(data["staticThreshold"]["psGelStaMin"]),
            int(data["staticThreshold"]["psGelStaMin"])
        ),
        "weekly_range": (
            int(data["minWeek"]),
            int(data["maxWeek"])
        ),
        "yearly_range": (
            int(data["minYear"]),
            int(data["maxYear"])
        ),
        "month_average_volume": data["qTotTran5JAvg"],
        "symbol": data["lVal18AFC"],
        "persian_name": data["lVal30"],
        "english_name": data["lVal18"],
        "instrument_id": data["instrumentID"],
        "ISIN": data["cIsin"],
        "number_of_shares": int(data["zTitad"]),
        "base_vloume": data["baseVol"],
        "flow_code": data["flow"],
        "flow_title": data["flowTitle"],
        "ُsector_code": int(data["sector"]["cSecVal"]),
        "sector_name": data["sector"]["lSecVal"],
        "EPS": data["eps"]["epsValue"] or data["eps"]["estimatedEPS"],
        "sector_pe": data["eps"]["sectorPE"],
        "PSR": data["eps"]["psr"],
        "free_float": data["kAjCapValCpsIdx"],
        "group": data["cgrValCot"],
        "group_title": data["cgrValCotTitle"],
        "y_value": data["yVal"],
        "nav": data["nav"]
    }


"""y_value:
263: سبد قابل معامله در بورس
300: سهام
301: اوراق مشارکت
302: سبد مشاع
303: اتیسی
304: آتی
306: اوراق مشارکت اتیسی
248: گواهي خريد سهام
068: شاخص
400: حق تقدم سهم
403: حق تقدم اتیسی
500: جايزه سهم"""


def all_tickers():
    url = URLs.ALL_TICKERS
    response = get(url)
    data = pd.read_html(response.text)[0]
    data.drop(0, axis='index', inplace=True)
    data.columns = ["ISIN", "group", "sector", "table",
                    "eng_symbol", "eng_name", "symbol", "name"]
    return data


def codal_announcement(days: int):
    url = URLs.GET_PREPARED_DATA.format(n=days)
    response = get(url)
    print(url)
    if response.status_code != 200:
        return None
    data = response.json()["preparedData"]
    data = pd.DataFrame(data)
    data = data.set_index("id")
    return data


def _supervisor_message(url):
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["msg"]
    if not data:
        return pd.DataFrame()
    data = pd.DataFrame(data)
    data.rename(
        columns={
            "tseMsgIdn": "id",
            "dEven": "date",
            "hEven": "time",
            "tseTitle": "title",
            "tseDesc": "description"
        },
        inplace=True
    )
    data.set_index("id", inplace=True)
    return data

    

def supervisor_message_by_insCode(insCode: int | str):
    url = URLs.GET_MESSAGE_BY_INSCODE.format(insCode=insCode)
    return _supervisor_message(url)


def supervisor_message_by_flow(flow: int, n: int = 10):
    if not 0 <= flow <= 4:
        return None
    url = URLs.GET_MESSAGE_BY_FLOW.format(flow=flow, n=n)
    return _supervisor_message(url)