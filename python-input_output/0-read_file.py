#!/usr/bin/python3
"""
This module provides a function read_file that reads a text file and prints
its content to the standard output. It demonstrates basic file handling in
Python, adhering to PEP 8 styling guidelines.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Parameters:
    filename (str): The name of file to be read. Defaults to an empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
