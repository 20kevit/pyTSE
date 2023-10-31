from download import *


class Ticker:
    def __init__(self, insCode):
        self.insCode = insCode

    def update_instrument_info(self):
        data = instrument_info(self.insCode)
        self.date = data["date"]
        self.down_limit = data["daily_threshold"][0]
        self.up_limit = data["daily_threshold"][1]
        self.week_low = data["weekly_range"][0]
        self.week_high = data["weekly_range"][1]
        self.year_low = data["yearly_range"][0]
        self.year_high = data["yearly_range"][1]

        self.symbol = data["symbol"]
        self.persian_name = data["persian_name"]
        self.english_name = data["english_name"]
        self.instrument_id = data["instrument_id"]
        self.ISIN = data["ISIN"]

        self.flow_code = data["flow_code"]
        self.flow_title = data["flow_title"]

        self.number_of_shares = data["number_of_shares"],
        self.base_vloume = data["base_vloume"]
        self.free_float = data["free_float"]
        self.month_average_volume = data["month_average_volume"]

        self.sector_code = data["sector_code"]
        self.sector_name = data["sector_name"]

        self.EPS = data["EPS"]
        self.sector_pe = data["sector_pe"]
        self.PSR = data["PSR"]

        self.group = data["group"]
        self.group_title = data["group_title"]
        self.y_value = data["y_value"]
        self.nav = data["nav"]
