#!/usr/bin/python3
"""It defines integer addition function."""


def add_integer(a, b=98):
    """It returns integer addition of a and b.

    Float arguments are typecasted - 
    ints before addition performed.

    Raises:
        TypeError: If a or b is non-integer and non-float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
