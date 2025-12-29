from src.converter import convert_currency

def test_conversion():
    assert convert_currency(100, 10) == 1000
