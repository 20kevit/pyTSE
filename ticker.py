from download import *


class Ticker:
    def __init__(self, insCode: int):
        self.insCode = insCode
        self.update_instrument_info()
        self.update_history()
        self.update_supervisor_message()
        self.update_instrument_state_changes()
        self.update_closing_price_info()
        self.update_best_limits()
        self.update_best_limits()
        self.update_client_type_history()
        self.update_trades()
        self.update_related_company()
        self.update_statistics()
        self.update_introduction()


    def update_instrument_info(self):
        print("hello")
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

    def update_history(self):
        data = history(self.insCode)
        self.history = data
    
    def update_supervisor_message(self):
        data = supervisor_message_by_insCode(self.insCode)
        self.supervisor_message = data
        
    def update_instrument_state_changes(self):
        data = instrument_state_changes(self.insCode)
        self.instrument_state_changes = data

    def update_closing_price_info(self):
        data = closing_price_info(self.insCode)
        self.status = data["status"]
        self.status_title = data["status_title"]
        self.last_update_time = data["last_update_time"]
        self.last_update_date = data["last_update_date"]
        self.low = data["low"]
        self.high = data["high"]
        self.close = data["close"]
        self.yesterday = data["yesterday"]
        self.first = data["first"]
        self.last = data["last"]
        self.number = data["number"]
        self.volume = data["volume"]
        self.value = data["value"]

    def update_best_limits(self):
        data = best_limits(self.insCode)
        self.asks = data["Asks"]
        self.bids = data["Bids"]

    def update_client_type_history(self):
        data = client_type_history(self.insCode)
        self.client_type_history = data

    def update_trades(self):
        data = trades(self.insCode)
        self.trades = data

    def update_related_company(self):
        data = related_company(self.sector_code)
        self.related_company = data

    def update_statistics(self):
        data = statistics(self.insCode)
        self.statistics = data

    def update_introduction(self):
        data = introduction(self.symbol)
        self.introduction = data
        