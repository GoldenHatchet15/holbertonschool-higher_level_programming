#!/usr/bin/python3
"""
This module defines the Rectangle class
with methods to calculate its area and perimeter,
and to represent it as a string using a custom symbol.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Methods:
    area(): Return the area of the rectangle.
    perimeter(): Return the perimeter of the rectangle,
    0 if either side is 0.
    __str__(): Return the string representation of
    the rectangle using the specified symbol(s).
    __repr__(): Return a string representation of the rectangle
    for recreation using eval().
    __del__(): Print a farewell message when an instance is deleted.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle, or 0 if either width or
        height is 0.

        Returns:
        int: The perimeter of the rectangle, or 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):

        """
        Returns a string representation of the rectangle using
        the specified symbol(s).

        Returns:
        str: A string representing the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        symbol = str(Rectangle.print_symbol)
        line = symbol * self._width
        body = (line + "\n") * (self._height - 1) + line
        return body

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate the instance using eval().

        Returns:
        str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Prints a farewell message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
