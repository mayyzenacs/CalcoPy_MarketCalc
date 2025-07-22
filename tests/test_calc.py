from source.mode import Calculator
import pytest

calc = Calculator()

def test_calc():
    result = calc.calc(2, '29.9')  
    assert result == 46.0

def test_mathFull ():
    assert calc.mathFull(6, 2) == 12
