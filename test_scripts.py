from scripts import func_zero, func_zero_above_python_10
import pytest


test_data = [(0, "zero"), (1, 1), (2, 2), (3, 3)]

@pytest.mark.parametrize(('input', 'result'), test_data)
def test_func_zero(input, result):
    assert func_zero(input) == result
    
@pytest.mark.parametrize(('input', 'result'), test_data)
def test_func_zero_above_python_10(input, result):
    assert func_zero_above_python_10(input) == result