import pytest
from src.main.Convertor import Convertor

def test_get_exchange_rate_USD(mocker):
    #arrange
    mock_value = "123456.789"
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    # act
    actual = convertor.get_exchange_rate("USD")    
    #assert
    assert actual == mock_value

def test_get_exchange_rate_GBP(mocker):
    #arrange
    mock_value = "222222.222"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    # act
    actual = convertor.get_exchange_rate("GBP")    
    #assert
    assert actual == mock_value

def test_get_exchange_rate_EUR(mocker):
    #arrange
    mock_value = "333333.333"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    # act
    actual = convertor.get_exchange_rate("EUR")    
    #assert
    assert actual == mock_value
    
def test_convert_bitcoin_to_USD(convertor):
    # act
    actual = convertor.convert_bitcoin("USD", 1)

    # assert
    expected = 120368.5
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