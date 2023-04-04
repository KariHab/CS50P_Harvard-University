from numb3rs import validate


def test_numbers():
    assert validate("255.255.255.255") == True
    assert validate("301.258.214.354") == False
    assert validate("450.0.0.0") == False
    assert validate("0.0.0.255") == True
    assert validate("1.400.500.800") == False
    assert validate("1.230.2000.0") == False 

def test_lenght():
    assert validate("1.1") == False
    assert validate("100.100.100.100") == True
    assert validate("100.100.100") == False
    assert validate("1.1.1") == False

def test_numeric():
    assert validate("cat") == False
    assert validate("1.1.1.1") == True
    assert validate(".!g.") == False

def test_formating():
    assert validate("1.1.1.1")== True
    assert validate("1,1,1,1") == False
    assert validate("1:1:1:1") == False
