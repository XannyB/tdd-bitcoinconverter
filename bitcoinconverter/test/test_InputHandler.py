from bitcoinconverter.src.InputHandler import InputHandler
import pytest

def test__set_currency_gbp(monkeypatch):
    input_handler = InputHandler()
    expected = "GBP"
    monkeypatch.setattr("builtins.input", lambda _: "gbp")

    result = input_handler._set_currency()
    
    assert result == expected

def test__set_currency_error(monkeypatch):
    input_handler = InputHandler()
    expected = -1
    monkeypatch.setattr("builtins.input", lambda _: "bbb")

    result = input_handler._set_currency()
    
    assert result == expected

def test__set_num_bitcoin_1(monkeypatch):
    input_handler = InputHandler()
    expected = 1.0
    monkeypatch.setattr("builtins.input", lambda _: 1.0)

    result = input_handler._set_num_bitcoin()

    assert result == expected

def test__set_num_bitcoin_minus(monkeypatch):
    input_handler = InputHandler()
    expected = -1
    monkeypatch.setattr("builtins.input", lambda _: -1.0)

    result = input_handler._set_num_bitcoin()

    assert result == expected

def test_get_currency_gbp(monkeypatch):
    input_handler = InputHandler()
    expected = "GBP"
    monkeypatch.setattr("builtins.input", lambda _: "gbp")

    result = input_handler.get_currency()
    
    assert result == expected

def test_get_currency_retries(monkeypatch):
    input_handler = InputHandler()
    expected = "GBP"
    inputs = iter(["xyz", "123", "gbp"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_handler.get_currency()
    
    assert result == expected

def test_get_num_bitcoin_retries(monkeypatch):
    input_handler = InputHandler()
    expected = 1.0
    inputs = iter(["xyz", -123, 1.0])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = input_handler.get_num_bitcoin()

    assert result == expected

