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

def test_convert_bitcoin_to_USD(mocker):
    #arrange
    mock_value = "111.11"
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    # act
    actual = convertor.convert_bitcoin("USD", 1) 
    expected = mock_value
    #assert
    assert actual == expected

def test_convert_two_bitcoin_to_USD(mocker):
    mock_value = 111.11 
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin("USD", 2)    
    expected = str(float(mock_value) * 2)

    assert actual == expected

def test_convert_bitcoin_to_GBP(mocker):
    mock_value = "222.22"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin("GBP", 1)    
    expected = mock_value
    
    assert actual == expected

def test_convert_two_bitcoin_to_GBP(mocker):
    mock_value = "222.22"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin("GBP", 2)    
    expected = str(float(mock_value) * 2)
    
    assert actual == expected

def test_convert_bitcoin_to_EUR(mocker):
    mock_value = "333.33"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin("EUR", 1)    
    expected = mock_value
    
    assert actual == expected

def test_convert_two_bitcoin_to_EUR(mocker):
    mock_value = "333.33"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin("EUR", 2)    
    expected = str(float(mock_value) * 2)
    
    assert actual == expected