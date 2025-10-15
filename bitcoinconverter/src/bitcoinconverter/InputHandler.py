from bitcoinconverter.Convertor import Convertor

class InputHandler:
    def __init__(self):    
        self.convertor = Convertor()

    def _set_currency(self):
        currency = input("Please enter currency you would you like to see conversion for: ")

        if currency in self.convertor.current_rates:
            return currency
        else:
            return -1

    def _set_num_bitcoin(self):
        try:
            num_bitcoin = float(input("Please enter bitcoin value: "))
            return num_bitcoin
        except:
            return -1

    def get_currency(self):
        while True:
            currency = self._set_currency()
            if currency != -1:
                return currency
            print("Please enter a supported currency type.")

    
    def get_num_bitcoin(self):
        while True:
            bitcoins = self._set_num_bitcoin()
            if bitcoins != -1 and bitcoins >= 0:
                return bitcoins
            print("Please enter a positive number.")


