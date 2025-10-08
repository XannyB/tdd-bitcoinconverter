from Convertor import Convertor
from InputHandler import InputHandler

def main():
    handler = InputHandler()

    try:
        currency_type = handler.get_currency()
    except:
        main()

    try:
        num_bitcoin = handler.get_num_bitcoin()
    except:
        main()        


    convertor = Convertor()
    converted_currency = convertor.convert_bitcoin(currency_type, num_bitcoin)

    if converted_currency != -1:
        print(f"Your bitcoin value is {converted_currency} in {currency_type}.")
    else:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()