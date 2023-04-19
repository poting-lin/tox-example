from typing import Union

def func_zero_above_python_10(n) -> int | str:
    # test shorthand (X | Y) syntax for Union for testing multiple python versions
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be non-negative integer')

    if n == 0:
        return "zero"
    else:
        return n


def func_zero(n) -> Union[int,str]:
    # test shorthand (X | Y) syntax for Union for testing multiple python versions
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be non-negative integer')

    if n == 0:
        return "zero"
    else:
        return n