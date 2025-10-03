from urllib.request import urlopen
import json

coinbase_rates_file = json.load(urlopen("https://api.coinbase.com/v2/exchange-rates?currency=BTC"))
currents_rates = coinbase_rates_file["data"]["rates"]

class Convertor():
    def get_exchange_rate(self, currency):
        if currency == "USD":
            return 100
        if currency == "GBP":
            return 200
        if currency == "EUR":
            return 300
    
    def convert_bitcoin(self, currency_type, coins):
        currency_total = 0;

        exchange_rate = currents_rates.get(currency_type)

        currency_total = exchange_rate * coins

        return currency_total