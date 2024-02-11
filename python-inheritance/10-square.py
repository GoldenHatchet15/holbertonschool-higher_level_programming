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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the print() and str() representation of the square.
        """
        return super().__str__()

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    # Example usage
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())
