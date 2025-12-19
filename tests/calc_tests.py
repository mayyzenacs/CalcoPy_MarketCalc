from src.math_mode import Calculator
import pytest

calc = Calculator()

def test_calc():
    result = calc.calc(2, '29.9')  
    assert result == 46.0

def test_calc_aritmetic(): 
    result = calc.calc(2, '34.9')
    assert result == 53.70

def test_calc_invalid_string():
    result = calc.calc(0, 'abc')
    assert result is None

def test_calc_zero_value():
    result = calc.calc(0, '0')
    assert result is None

def test_calc_large_value():
    result = calc.calc(0, '900000,0000')
    assert result is None

def test_mathFull ():
    assert calc.mathFull(6, 2) == 12
