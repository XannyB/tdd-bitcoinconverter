from bitcoinconverter.InputHandler import InputHandler
from bitcoinconverter.Convertor import Convertor

def main(test_mode=False):
    handler = InputHandler()

    while True:
        currency = get_currency_type_input(handler)
        bitcoin = get_bitcoin_input(handler)        
        print(get_conversion(currency, bitcoin))
        if test_mode:
            break

def get_currency_type_input(handler):
    currency = handler.get_currency()
    return currency

def get_bitcoin_input(handler):
    bitcoin = handler.get_num_bitcoin()
    return bitcoin

def get_conversion(currency_type, num_bitcoin):
    convertor = Convertor()
    converted_currency = convertor.convert_bitcoin(currency_type, num_bitcoin)

    if converted_currency != -1:
        return f"Your bitcoin value is {converted_currency} in {currency_type}."
    else:
        return "An error has occurred. Please try again."

if __name__ == "__main__":
    main()