import pytest
from plates import is_valid

def test_alphabetical():
    assert is_valid("AB") == True
    assert is_valid("A2") == False
    assert is_valid ("3A") == False
    assert is_valid("22") == False
    assert is_valid("1") == False

def test_numberplacement():
    assert is_valid("A22CV") == False
    assert is_valid("A2CV2") == False
    assert is_valid("AC2V") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False
    assert is_valid("ABCDE") == True

def test_zeroplacement():
    assert is_valid("AC0CD") == False
    assert is_valid("ACC20") == True
    assert is_valid("A0C") == False
    assert is_valid("AAC02") == False


def test_alphanumeric():
    assert is_valid("!AXC") == False
    assert is_valid(".!,:;") == False
    assert is_valid("-!?,") == False
    assert is_valid("A!.,") == False
    assert is_valid("AC.VC") == False



