#!/usr/bin/python3
"""
This module provides a function text_indentation that prints a text
with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in special_chars:
            print(new_text.strip())
            print()
            new_text = ""
    print(new_text.strip(), end="")
