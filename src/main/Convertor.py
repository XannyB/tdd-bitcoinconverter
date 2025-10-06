from urllib.request import urlopen
import json

class Convertor:
    def __init__(self):
        self.current_rates = self._fetch_rates()

    def _fetch_rates(self):
        coinbase_rates_file = json.load(urlopen("https://api.coinbase.com/v2/exchange-rates?currency=BTC"))
        return coinbase_rates_file["data"]["rates"]

    def get_exchange_rate(self, currency):
        return self.current_rates[currency]
    
    def convert_bitcoin(self, currency_type, coins):
        currency_total = 0
        exchange_rate = self.get_exchange_rate(currency_type)
        currency_total = float(exchange_rate) * coins
        print(currency_total)
        return currency_total
    
convertor = Convertor()
convertor.convert_bitcoin("USD", 1)
convertor.convert_bitcoin("USD", 2)