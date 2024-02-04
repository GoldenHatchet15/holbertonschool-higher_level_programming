#!/usr/bin/python3
"""
This module provides a function
say_my_name which prints the full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
