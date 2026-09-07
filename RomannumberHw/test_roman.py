
import pytest
from roman import convert


def test_basic_symbols():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10


def test_multiple_symbols():
    assert convert("II") == 2
    assert convert("III") == 3
    assert convert("VI") == 6
    assert convert("XVI") == 16


def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90


def test_combination():
    assert convert("XIX") == 19
    assert convert("XVII") == 17

    import pytest


def test_invalid_roman():
    with pytest.raises(ValueError):
        convert("XQW")


