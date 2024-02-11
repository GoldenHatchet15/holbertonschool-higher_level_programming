#!/usr/bin/python3
"""
This module defines the MyList class which inherits from the built-in list class.
"""


class MyList(list):
    """
    MyList class that inherits from list.

    Methods:
        print_sorted(self): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without modifying the original list.
        """
        print(sorted(self))
