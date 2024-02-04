#!/usr/bin/python3
"""
This module provides an add_integer function that adds two integers.
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
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
