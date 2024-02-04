#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with a list containing one integer
        self.assertEqual(max_integer([3]), 3)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list of integers and negative integers
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list of non-integer types
        self.assertRaises(TypeError, max_integer, [None])
        self.assertRaises(TypeError, max_integer, ["string", 2, 3, 4])
        self.assertRaises(TypeError, max_integer, [1.1, 2.2, 3.3, 4.4])

if __name__ == '__main__':
    unittest.main()
