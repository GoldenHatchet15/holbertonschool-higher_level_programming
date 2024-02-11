#!/usr/bin/python3
"""
This module defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    An empty class.
    """
    pass


if __name__ == "__main__":
    # Example usage
    BaseGeometry = __import__('5-base_geometry').BaseGeometry

    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
