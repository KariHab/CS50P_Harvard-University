from twttr import shorten


def test_twttr():
    assert shorten("manger") == "mngr"
    assert shorten("tele") == "tl"
    assert shorten("taeiou") == "t"
    assert shorten("MANGER") == "MNGR"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"