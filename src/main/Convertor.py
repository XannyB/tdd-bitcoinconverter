class Convertor():
    def get_exchange_rate(self, currency):
        if currency == "USD":
            return 100
        if currency == "GBP":
            return 200
        if currency == "EUR":
            return 300
    
    def convert_bitcoin(self, currency, coins):
        num_currency = 0;

        exchange_rate = self.get_exchange_rate(currency)

        num_currency = exchange_rate * coins

        return num_currency