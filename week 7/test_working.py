from working import convert
import pytest


def test_goodformat():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_falseminutes():
    with pytest.raises(ValueError):
         convert("8:60 AM to 4:60 PM")

def test_falsehours():
    with pytest.raises(ValueError):
          convert("14 PM to 14 AM")


def test_format():
    with pytest.raises(ValueError):
         convert("9AM - 5PM")     
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

