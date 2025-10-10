from urllib.request import urlopen
from enum import Enum

import json

class Convertor:
    def __init__(self):
        try:
            self.current_rates = self._fetch_rates()
        except OSError:
            self.current_rates = -1

    def _fetch_rates(self):
            url = urlopen("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
            return json.load(url)["data"]["rates"]
        
    class Currency(Enum):
        USD = "USD"
        GBP = "GBP"
        EUR = "EUR"

    def get_exchange_rate(self, currency):
        return float(self.current_rates[currency])
    
    def convert_bitcoin(self, currency_type, coins):
        currency_total = 0
        exchange_rate = float(self.get_exchange_rate(currency_type))

        if coins >= 0 and exchange_rate >= 0:
            currency_total = round((exchange_rate * coins), 2)

        else:
            currency_total = -1

        return currency_total
