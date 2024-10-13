import pytest
from project import price, exchange, top

def test_price():
    with pytest.raises(SystemExit):
        price("123")

def test_exchange():
    with pytest.raises(SystemExit):
        exchange("123")
    assert exchange("USD") == 1

def test_top():
    with pytest.raises(SystemExit):
        top("A")
