#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file (UTF-8)
and returns the number of characters written. It demonstrates file writing
capabilities in Python, following PEP 8 styling guidelines and best practices
for file handling.
"""


def write_file(filename="", text=""):
    """
    Writes string to text file (UTF-8), returns number of characters written.

    Args:
    filename (str): Name of file to write to. Defaults to an empty string.
    text (str):  text to write into file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
