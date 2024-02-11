#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class for future geometric shapes.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    # Example usage
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
