#!/usr/bin/python3
"""
This module defines the inherits_from function that checks if an object
is an instance of a class that inherited (directly or indirectly) from
the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class;
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
