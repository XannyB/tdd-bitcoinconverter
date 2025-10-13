import pytest
from src.bitcoinconvertor.main import main
from src.bitcoinconvertor.main import get_currency_type_input
from src.bitcoinconvertor.Convertor import Convertor
from src.bitcoinconvertor.InputHandler import InputHandler

def test_main(monkeypatch, mocker, capsys):
    mock_value = "100.0"
    mock_data = {"GBP": mock_value}
    monkeypatch.setattr(InputHandler, "get_currency", lambda _: "GBP")
    monkeypatch.setattr(InputHandler, "get_num_bitcoin", lambda _: 1.0)

    mocker.patch.object(Convertor,"_fetch_rates", return_value=mock_data)
    main()    

    expected = "Your bitcoin value is 100.0 in GBP.\n"
    actual = capsys.readouterr()

    assert actual.out == expected

def test_currency_input_fail(monkeypatch, mocker, capsys):
    mock_value = "100.0"
    mock_data = {"GBP": mock_value}
    monkeypatch.setattr(InputHandler, "get_currency", lambda _: "GBP")
    monkeypatch.setattr(InputHandler, "get_num_bitcoin", lambda _: 1.0)    
    mocker.patch.object(Convertor,"convert_bitcoin", return_value= -1)
    main()    

    expected = "An error has occurred. Please try again.\n"
    actual = capsys.readouterr()

    assert actual.out == expected

