import pytest
from plates import is_valid

def test_plate():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False
    assert is_valid("C") == False
    assert is_valid("BLAHHHH") == False
    assert is_valid("HICS50") == True
    assert is_valid("QQQQ23") == True
    assert is_valid("QQQQ03") == False
    assert is_valid("QQQ23Q") == False
    assert is_valid("CS50$$") == False
