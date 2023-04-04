from um import count
import pytest

def test_word():
    assert count("am") == 0
    assert count("um") == 1
    assert count("Um") == 1

def test_alpha():
    assert count("um!") == 1
    assert count("um?") == 1

def test_inword():
    assert count ("Um") == 1
    assert count ("Um Um") == 2
    assert count ("yummy") == 0

