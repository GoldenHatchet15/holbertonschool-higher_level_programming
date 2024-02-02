#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size with getter and setter, and a method to print the square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.
        
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character."""
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
