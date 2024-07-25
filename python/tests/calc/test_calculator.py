import pytest

from python.app.subdir.calculator import Calculator

def test_list_int():
    data = [1, 2, 3]
    calc = Calculator()
    result = calc.sum(data)
    
    assert result == 6
def test_add():
    calc = Calculator()
    result = calc.add(1, 2)
    assert result == 3
def test_subtract():
    calc = Calculator()
    result = calc.subtract(4, 1)
    assert result == 3
def test_multiply():
    calc = Calculator()
    result = calc.multiply(3, 3)
    assert result == 9
def test_divide():
    calc = Calculator()
    result = calc.divide(9,3)
    assert result == 3

def test_divide_by_zero_raises_exception():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(9, 0)
