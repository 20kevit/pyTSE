import requests 
import pandas as pd
import URLs

USER_AGENT = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
def get(url):
    return requests.get(
        url = url,
        headers = {"User-Agent" : USER_AGENT}
    )

def history(insCode:int|str, days:int=0) -> pd.DataFrame:
    days = 0 if days < 0 else days
    url = URLs.CLOSING_PRICE_DAILY_LIST.format(
        insCode = insCode,
        n = days
    )
    response = get(url).json()["closingPriceDaily"]
    if not response:
        return pd.DataFrame()
    data = pd.DataFrame(response)
    data.drop(
        columns=["last", "id", "insCode", "hEven", "iClose", "yClose", "priceChange"],
        inplace=True
    )
    data.rename(
        columns={
            "priceMin" : "low",
            "priceMax" : "high",
            "priceYesterday" : "yesterday",
            "priceFirst" : "first",
            "dEven" : "date",
            "pClosing" : "close",
            "pDrCotVal" : "last",
            "zTotTran" : "number", #number of transactions
            "qTotTran5J" : "volume", #volume of transactions
            "qTotCap" : "value" #value of transactions
        },
        inplace=True
    )
    data.set_index('date', inplace=True)
    data = data.astype(dtype='int64')

    return data

def instrument_info(insCode:int|str):
    url = URLs.TICKER_INSTRUMENT_INFO.format(insCode)
    response = get(url)
    if response.status_code != 200:
        return None
    data = response.json()["instrumentInfo"]
    print(data["kAjCapValCpsIdx"])
    return {
        "date" : data["dEven"],
        "daily_threshold" : (
            int(data["staticThreshold"]["psGelStaMin"]),
            int(data["staticThreshold"]["psGelStaMin"])
            ),
        "weekly_range" : (
            int(data["minWeek"]),
            int(data["maxWeek"])
        ),
        "yearly_range" : (
            int(data["minYear"]),
            int(data["maxYear"])            
        ),
        "month_average_volume" : data["qTotTran5JAvg"],
        "symbol" : data["lVal18AFC"],
        "persian_name" : data["lVal30"],
        "english_name" : data["lVal18"],
        "instrument_id" : data["instrumentID"],
        "ISIN" : data["cIsin"],
        "number_of_shares" : int(data["zTitad"]),
        "base_vloume" : data["baseVol"],
        "flow_code" : data["flow"],
        "ُsector_code" : int(data["sector"]["cSecVal"]),
        "sector_name" : data["sector"]["lSecVal"],
        "EPS" : data["eps"]["epsValue"] or data["eps"]["estimatedEPS"],
        "sector_pe" : data["eps"]["sectorPE"],
        "PSR" : data["eps"]["psr"]
    }