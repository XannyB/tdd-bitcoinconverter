from src.main.Convertor import Convertor

def test_get_exchange_rate_USD():
    # arrange
    convertor = Convertor()

    # act
    actual = convertor.get_exchange_rate("USD")

    # assert
    expected = 100
    assert (actual == expected)