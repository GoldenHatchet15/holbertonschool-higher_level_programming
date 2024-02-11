#!/usr/bin/python3
"""
This module provides a function to_json_string that serializes an object to a
JSON formatted string. It demonstrates the use of the json module for
serialization purposes, catering to the need for converting Python data
structures to a format that can be easily shared between programs or stored
for later use.

The function defined within handles the conversion of objects like lists and
dictionaries to their JSON string representation, emphasizing simplicity and
the utility of Python's standard library for common programming tasks.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    The function utilizes the json.dumps() method to serialize the provided
    object (my_obj) into a JSON formatted string. This can be particularly
    useful for converting Python data structures to a text format that is
    easily readable, can be stored, or transmitted over a network.

    Args:
        my_obj: The object to serialize to a JSON formatted string. This can
                be any object that json.dumps() can serialize, typically
                including native Python data structures like dictionaries,
                lists, strings, numbers, and boolean values.

    Returns:
        A string containing the JSON representation of the provided object.
        If the object cannot be serialized, a TypeError will be raised by
        the json.dumps() method.

    Note:
        The function does not handle exceptions internally, leaving exception
        management to the caller.
    """
    return json.dumps(my_obj)
