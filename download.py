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