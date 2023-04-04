from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    with pytest.raises (ValueError):
        convert("5/2")
    with pytest.raises (ZeroDivisionError):
        convert ("1/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    if convert ("1/2") == 50:
        assert gauge(50) == "50%"
