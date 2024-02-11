#!/usr/bin/python3
"""
This module defines a function save_to_json_file that writes an object to a
text file, using a JSON representation. It demonstrates the use of the json
module for serialization of Python objects into JSON format and writing the
result to files, adhering to the principles of resource management and
error handling in Python.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize into JSON format.
        filename (str): name of file where JSON string will be written.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
