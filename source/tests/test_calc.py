from mode import Calculator

calc = Calculator()

def test_calc():
    result = calc.calc(2, '29.9')  
    assert result == 46.0

def test_mathFull ():
    assert calc.mathFull(12, 6) == 72