#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square."""
    
    def __init__(self, size):
        """Initialize the square."""
        super().integer_validator("size", size)  # Corrected reference to "size"
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
    
    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"
