#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        Validates size as a positive integer.
        """
        super().__init__(size, size)  # Call to the superclass __init__ with size as both width and height
        self.__size = size  # Private attribute __size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description for print() and str().
        """
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    # Example usage
    Square = __import__('11-square').Square

    s = Square(13)

    print(s)
    print(s.area())
