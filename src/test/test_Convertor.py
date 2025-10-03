from src.main.Convertor import Convertor

# arrange
convertor = Convertor()

def test_get_exchange_rate_USD():
    # act
    actual = convertor.get_exchange_rate("USD")

    # assert
    expected = 100
    assert (actual == expected)

def test_get_exchange_rate_GBR():
    # act
    actual = convertor.get_exchange_rate("GBR")

    # assert
    expected = 200
    assert (actual == expected)