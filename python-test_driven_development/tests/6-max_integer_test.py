#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_invalid_input(self):
        """Test lists with invalid input."""
        self.assertRaises(TypeError, max_integer, ["string", 2, 3, 4])
        self.assertRaises(TypeError, max_integer, [None, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
