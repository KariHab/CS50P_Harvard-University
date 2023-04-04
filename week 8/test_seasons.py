from seasons import get_birthday
import pytest

def test_date():
    assert get_birthday("2021-10-11") == "Five hundred twenty-five thousand, six hundred minutes"