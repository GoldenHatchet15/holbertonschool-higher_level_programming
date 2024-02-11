#!/usr/bin/python3
"""
This module defines a function load_from_json_file that creates an object
from a JSON file. Leveraging the json module's load method, it exemplifies
how to read and deserialize JSON formatted data from files into Python
objects, such as dictionaries and lists. This facilitates the easy retrieval
of structured data stored in files, adhering to best practices for resource
management and file handling in Python.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): name of file containing JSON data to deserialize.

    Returns:
        The Python object resulting from the deserialization of the JSON data
        contained in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
