from urllib.request import urlopen
from urllib.error import HTTPError, URLError

import json

class Convertor:
    def __init__(self):
        self.current_rates = self._fetch_rates()

    def _fetch_rates(self):
        try:
            url = urlopen("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
            return json.load(url)["data"]["rates"]
        except:
            {}

    def get_exchange_rate(self, currency):
        return self.current_rates[currency]
    
    def convert_bitcoin(self, currency_type, coins):
        currency_total = 0
        exchange_rate = self.get_exchange_rate(currency_type)
        currency_total = float(exchange_rate) * coins
        return str(currency_total)
    
convertor = Convertor()