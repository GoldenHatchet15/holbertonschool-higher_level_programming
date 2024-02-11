#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Validates width and height as positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    # Example usage
    Rectangle = __import__('9-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())
