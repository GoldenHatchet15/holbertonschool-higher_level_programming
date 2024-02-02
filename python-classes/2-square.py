#!/usr/bin/python3
"""Defines a class Square
with a private instance attribute size
and validates the size."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
