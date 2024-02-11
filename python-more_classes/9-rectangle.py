#!/usr/bin/python3
"""
This module defines the Rectangle class with methods to calculate its area
and perimeter, represent it as a string using a custom symbol, compare the
area of two rectangles, and create a square as a special case of a rectangle.
"""


class Rectangle:
    """
    A class to represent a rectangle.
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
        """Returns the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle, or 0 if either side is 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self._width == 0 or self._height == 0:
            return ""
        symbol = str(Rectangle.print_symbol)
        line = symbol * self._width
        body = (line + "\n") * (self._height - 1) + line
        return body

    def __repr__(self):
        """Returns a string representation for recreation using eval()."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area or rect_1 if both
        have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
