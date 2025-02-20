import pytest
from numb3rs import validate

def test_validate():
    assert(validate("1.2.3.256")) == False
    assert(validate("1.2.256.3")) == False
    assert(validate("1.256.2.3")) == False
    assert(validate("256.1.2.3")) == False
    assert(validate("1.2.3.4")) == True


