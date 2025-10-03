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
