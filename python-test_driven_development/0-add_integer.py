#!/usr/bin/python3
"""
This module provides an add_integer function
that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: The first parameter, must be an integer or float.
        b: The second parameter, must be an integer or float (defaults to 98).

    Returns:
        The sum of a and b, converted to an integer.

    Raises:
        TypeError: If either of a or b is neither an integer nor a float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
