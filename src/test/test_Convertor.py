from src.bitcoinconvertor.Convertor import Convertor
from urllib.error import URLError
import pytest

def test_get_exchange_rate_USD(mocker):
    #arrangemock_value
    mock_value = "123456.789"
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    expected = float(mock_value)
    # act
    actual = convertor.get_exchange_rate(convertor.Currency.USD.value)    
    #assert
    assert actual == expected

def test_get_exchange_rate_GBP(mocker):
    #arrange
    mock_value = "222222.222"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    expected = float(mock_value)
    # act
    actual = convertor.get_exchange_rate(convertor.Currency.GBP.value)    
    #assert
    assert actual == expected

def test_get_exchange_rate_EUR(mocker):
    #arrange
    mock_value = "333333.333"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    expected = float(mock_value)
    # act
    actual = convertor.get_exchange_rate(convertor.Currency.EUR.value)    
    #assert
    assert actual == expected

def test_get_exchange_IOError(mocker):
    #arrange
    mocker.patch("src.bitcoinconvertor.Convertor.urlopen", side_effect=IOError("Simulated Network/Disk Issue."))
    convertor = Convertor()
    expected = -1

    actual = convertor.current_rates 

    assert actual == expected

def test_get_rates_URLError(mocker):
    #arrange
    mocker.patch("src.bitcoinconvertor.Convertor.urlopen", side_effect=URLError("URL Not Found!"))
    convertor = Convertor()
    expected = -1

    actual = convertor.current_rates 

    assert actual == expected

def test_get_exchange_rate_OSError(mocker):
    mocker.patch.object(Convertor,"_fetch_rates", side_effect=OSError("Simulation: Site doesn't exist!"))
    convertor = Convertor()
    expected = -1

    actual = convertor.current_rates

    assert actual == expected

def test_convert_bitcoin_to_USD(mocker):
    #arrange
    mock_value = "111.11"
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    # act
    actual = convertor.convert_bitcoin(convertor.Currency.USD.value, 1) 
    expected = float(mock_value)
    #assert
    assert actual == expected

def test_convert_two_bitcoin_to_USD(mocker):
    mock_value = 111.11 
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()

    actual = convertor.convert_bitcoin(convertor.Currency.USD.value, 2)    
    expected = float(mock_value) * 2

    assert actual == expected

def test_convert_bitcoin_to_GBP(mocker):
    mock_value = "222.22"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()    
    expected = float(mock_value)

    actual = convertor.convert_bitcoin(convertor.Currency.GBP.value, 1)
    
    assert actual == expected

def test_convert_two_bitcoin_to_GBP(mocker):
    mock_value = "222.22"
    mock_data = {"GBP": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()    
    expected = float(mock_value) * 2

    actual = convertor.convert_bitcoin(convertor.Currency.GBP.value, 2)
    
    assert actual == expected

def test_convert_bitcoin_to_EUR(mocker):
    mock_value = "333.33"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()    
    expected = float(mock_value)

    actual = convertor.convert_bitcoin(convertor.Currency.EUR.value, 1)
    
    assert actual == expected

def test_convert_two_bitcoin_to_EUR(mocker):
    mock_value = "333.33"
    mock_data = {"EUR": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()    
    expected = float(mock_value) * 2

    actual = convertor.convert_bitcoin(convertor.Currency.EUR.value, 2)
    
    assert actual == expected

def test_convert_0_bitcoin_to_USD(mocker):
    mock_value = "0.0"
    mock_data = {"USD": mock_value}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()    
    expected = float(mock_value)

    actual = convertor.convert_bitcoin(convertor.Currency.USD.value, 0)
    
    assert actual == expected

def test_convert_negative_bitcoin_to_USD(mocker):
    mock_data = {"USD": "-1.0"}
    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    convertor = Convertor()
    expected = -1

    actual = convertor.convert_bitcoin(convertor.Currency.USD.value, -1)    
    
    assert actual == expected

