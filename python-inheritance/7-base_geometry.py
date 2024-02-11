#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Method not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as an integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
