#!/usr/bin/python3
"""
Module 2-is_same_class defines a function is_same_class that checks
if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
              otherwise False.
    """
    return type(obj) is a_class


if __name__ == "__main__":
    # Example usage
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
