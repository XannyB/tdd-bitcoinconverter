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
            return -1

    def get_exchange_rate(self, currency):
        if self.current_rates != -1:
            return self.current_rates[currency]
        else:
            return -1
    
    def convert_bitcoin(self, currency_type, coins):
        currency_total = 0
        
        exchange_rate = float(self.get_exchange_rate(currency_type))

        if exchange_rate >= 0:
            currency_total = exchange_rate * coins
        else:
            currency_total = -1

        return str(currency_total)
    
convertor = Convertor()