from python.app.subdir.calculator import Calculator 

def test_list_int():
    """
    Test that it can sum a list of integers
    """
    data = [1, 2, 3]
    calc = Calculator()
    result = calc.sum(data)
    
    assert result == 6
def test_add():
    """
    Test that it can add two integers
    """
    calc = Calculator()
    result = calc.add(1, 2)
    assert result == 3
def test_subtract():
    """
    Test that it can subtract two integers
    """
    calc = Calculator()
    result = calc.subtract(4, 1)
    assert result == 3
def test_multiply():
    """
    Test that it can multiply two integers
    """
    calc = Calculator()
    result = calc.multiply(3, 3)
    assert result == 9
def test_divide():
    """
    Test that it can divide two integers
    """
    calc = Calculator()
    result = calc.divide(9,3)
    assert result == 3
