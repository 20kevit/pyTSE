import requests
import pandas as pd
import URLs
from tools import *

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
    data["date"] = data["date"].apply(dEven_to_date)
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
        "date": dEven_to_date(data["dEven"]),
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
        "sector_code": int(data["sector"]["cSecVal"]),
        "sector_name": data["sector"]["lSecVal"],
        "EPS": int(data["eps"]["epsValue"] or data["eps"]["estimatedEPS"]),
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
    data["date"] = data["date"].apply(dEven_to_date)
    data["time"] = data["time"].apply(hEven_to_time)
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


def instrument_state_changes(insCode=None, n=10):
    """n will be ignored if insCode is declared"""
    if insCode:
        url = URLs.ALL_INSTRUMENT_STATE_CHANGES.format(insCode=insCode)
    else:
        url = URLs.TOP_INSTRUMENT_STATE_CHANGES.format(n=n)

    response = get(url)
    data = response.json()["instrumentState"]
    data = pd.DataFrame(data)
    data.rename(
        columns={
            "idn": "id",
            "dEven": "date",
            "hEven": "time",
            "insCode": "insCode",
            "lVal18AFC": "symbol",
            "lVal30": "name",
            "cEtaval": "status",
            "cEtavalTitle": "status_title"
        },
        inplace=True
    )
    drop_list = ["realHeven", "underSupervision"]
    if insCode:
        drop_list += ["insCode", "symbol", "name", "id"]
    else:
        data.set_index("id", inplace=True)
    data.drop(
        columns=drop_list,
        inplace=True
    )
    data["date"] = data["date"].apply(dEven_to_date)
    data["time"] = data["time"].apply(hEven_to_time)
    return data


def closing_price_info(insCode: int | str):
    url = URLs.GET_CLOSING_PRICE_INFO.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["closingPriceInfo"]
    return {
        "status": data["instrumentState"]["cEtaval"],
        "status_title": data["instrumentState"]["cEtavalTitle"],
        "last_update_time": hEven_to_time(data["lastHEven"]),
        "last_update_date": dEven_to_date(data["finalLastDate"]),
        "low": int(data["priceMin"]),
        "high": int(data["priceMax"]),
        "close": int(data["pClosing"]),
        "yesterday": int(data["priceYesterday"]),
        "first": int(data["priceFirst"]),
        "last": int(data["pDrCotVal"]),
        "number" : int(data["zTotTran"]),
        "volume": int(data["qTotTran5J"]),
        "value": int(data["qTotCap"])
    }


def best_limits(insCode: int | str):
    url = URLs.BEST_LIMITS.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["bestLimits"]
    data = pd.DataFrame(data)
    asks = data[["zOrdMeDem", "qTitMeDem", "pMeDem"]].astype(int)
    bids = data[["zOrdMeOf", "qTitMeOf", "pMeOf"]].astype(int)
    asks.rename(
        columns={
            "zOrdMeDem": "number",
            "qTitMeDem": "volume",
            "pMeDem": "price"
        },
        inplace=True
    )
    bids.rename(
        columns={
            "zOrdMeOf": "number",
            "qTitMeOf": "volume",
            "pMeOf": "price"
        },
        inplace=True
    )
    return {
        "Asks": asks,
        "Bids": bids
    }
    

def client_type_history(insCode: int | str):
    url = URLs.GET_CLIENT_TYPE_HISTORY.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["clientType"]
    data = pd.DataFrame(data)
    data.drop(columns=["insCode"], inplace=True)
    data.rename(
        columns={
            "recDate": "date",
            "buy_I_Count": "individual_buy_count",
            "buy_I_Volume": "individual_buy_volume",
            "buy_I_Value": "individual_buy_value",
            "sell_I_Count": "individual_sell_count",
            "sell_I_Volume": "individual_sell_volume",
            "sell_I_Value": "individual_sell_value",
            "buy_N_Count": "juridical_buy_count",
            "buy_N_Volume": "juridical_buy_volume",
            "buy_N_Value": "juridical_buy_value",
            "sell_N_Count": "juridical_sell_count",
            "sell_N_Volume": "juridical_sell_volume",
            "sell_N_Value": "juridical_sell_value",
        },
        inplace=True
    )
    data["date"] = data["date"].apply(dEven_to_date)
    data.set_index("date", inplace=True)
    data = data.astype("Int64")
    return data


def trades(insCode: int | str):
    url = URLs.GET_TRADE.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["trade"]
    data = pd.DataFrame(data)
    data.drop(
        columns=[
            "insCode", "dEven","nTran", "qTitNgJ", "iSensVarP", "pPhSeaCotJ", "pPbSeaCotJ", "iAnuTran", "xqVarPJDrPRf"
        ],
        inplace=True
    )
    data.rename(
        columns={
            "hEven": "time",
            "qTitTran": "volume",
            "pTran": "price"
        },
        inplace=True
    )
    data["price"] = data["price"].astype(int)
    data["canceled"] = data["canceled"].astype(bool)
    data["time"] = data["time"].apply(hEven_to_time)
    return data


def related_company(group_code: int | str):
    url = URLs.GET_RELATED_COMPANY.format(group_code=group_code)
    response = get(url)
    if response.status_code != 200:
        return None
    related_company = response.json()["relatedCompany"]
    result = list()
    for company in related_company:
        result.append(
            {
                "insCode": company["instrument"]["insCode"],
                "name": company["instrument"]["lVal30"],
                "symbol": company["instrument"]["lVal18AFC"],
            }
        )
    data = pd.DataFrame(result)
    return data


def statistics(insCode: int | str):
    url = URLs.GET_INSTRUMENT_STATISTICS.format(insCode=insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["instrumentStatistic"]
    data = pd.DataFrame(data)
    data.drop(
        columns=["insCode", "dEven"],
        inplace=True
    )
    data.rename(
        columns={
            "dataType": "code",
            "dataValue": "value",
            "dataTypeDesc": "description",
            "partitionCode": "type"
        },
        inplace=True
    )
    data.type.replace(
        {
            1: "negative_days",
            2: "positive_days",
            3: "no_trade_days",
            4: "number_of_transactions",
            5: "value_of_transactions",
            6: "value_of_company",
            7: "volume_of_transactions",
            8: "closing_price",
            9: "open_or_close_days",
            10: "number_of_sellers_or_buyers",
            11: "client_type"
        },
        inplace=True
    )
    data.set_index("code", inplace=True)
    return data


def introduction(symbol: str):
    url = URLs.GET_CODAL_PUBLISHER_BY_SYMBOL.format(symbol=symbol)
    response = get(url)
    if response.status_code != 200:
        return None
    return response.json()["codalPublisher"]