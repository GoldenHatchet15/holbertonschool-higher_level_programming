#!/usr/bin/python3
"""
This module defines a lookup function
that returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    This function uses the built-in dir() method to find the attributes
    and methods of an object.

    Args:
        obj: The object for which to list attributes and methods.

    Returns:
        A list of strings, where each string is an attribute or method name.
    """
    return dir(obj)
