from src.calculator import Calculator
import pytest
import sys


class TestCalculator(object):
    def test_add_no_input(self):
        with pytest.raises(TypeError):
            calc = Calculator()

    def test_add_single_input(self):
        with pytest.raises(TypeError):
            calc = Calculator()

    def test_add_str_input(self):
        with pytest.raises(ValueError):
            calc = Calculator('a', 'b')

    def test_add_float_input(self):
        calc = Calculator(1.453, 65.7766)
        actual = calc.add()
        expected = pytest.approx(67.2296)
        assert actual == expected, f'Actual: {actual}, Expected: {expected}'

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calc = Calculator(1, 0)
            calc.div()

    # we skip the below test if python version is greater than 3.x
    @pytest.mark.skipif(sys.version_info > (3, 0), reason=f"skipping as python version is {sys.version.split(' | ')[0]}")
    def test_skip(self):
        raise Exception('Python version needed is 2.x')


