#!/usr/bin/python3
"""
This module defines the Rectangle class
with methods to calculate its area and perimeter,
and to represent it as a string using the "#" character.
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
    the rectangle using "#" characters.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
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
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        return ("#" * self._width + "\n") * (self._height - 1) + "#" * self._width
