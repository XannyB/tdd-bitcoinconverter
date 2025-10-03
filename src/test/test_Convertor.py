import pytest
from src.main.Convertor import Convertor

# arrange
@pytest.fixture
def convertor():
    return Convertor()

def test_get_exchange_rate_USD(convertor):
    # act
    actual = convertor.get_exchange_rate("USD")

    # assert
    expected = 100
    assert actual == expected

def test_get_exchange_rate_GBP(convertor):
    # act
    actual = convertor.get_exchange_rate("GBP")

    # assert
    expected = 200
    assert actual == expected

def test_get_exchange_rate_EUR(convertor):
    # act
    actual = convertor.get_exchange_rate("EUR")

    # assert
    expected = 300
    assert actual == expected

def test_convert_bitcoin_to_USD(convertor):
    # act
    actual = convertor.convert_bitcoin("USD", 1)

    # assert
    expected = 100
    assert actual == expected

def test_convert_two_bitcoin_to_USD(convertor):
    # act
    actual = convertor.convert_bitcoin("USD", 2)

    # assert
    expected = 200
    assert actual == expected

def test_convert_bitcoin_to_GBP(convertor):
    # act
    actual = convertor.convert_bitcoin("GBP", 1)

    # assert
    expected = 200
    assert actual == expected

def test_convert_two_bitcoin_to_GBP(convertor):
    # act
    actual = convertor.convert_bitcoin("GBP", 2)

    # assert
    expected = 400
    assert actual == expected

def test_convert_bitcoin_to_EUR(convertor):
    # act
    actual = convertor.convert_bitcoin("EUR", 1)

    # assert
    expected = 300
    assert actual == expected

def test_convert_two_bitcoin_to_EUR(convertor):
    # act
    actual = convertor.convert_bitcoin("EUR", 2)

    # assert
    expected = 600
    assert actual == expected