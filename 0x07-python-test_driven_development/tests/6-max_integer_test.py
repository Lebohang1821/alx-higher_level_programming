#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

import unittest

class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer function."""

    def test_empty_list(self):
        """Test for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """Test for no arguments passed to the function."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test for a list with only one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_positive_end(self):
        """Test for a list of all positive numbers with the max at the end."""
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)

    def test_positive_middle(self):
        """Test for a list of all positive numbers with the max in the middle."""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_positive_beginning(self):
        """Test for a list of all positive numbers with the max at the beginning."""
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50]), 200)

    def test_one_negative(self):
        """Test for a list with one negative number."""
        self.assertEqual(max_integer([200, 10, 8, -36, 14, 50]), 200)

    def test_all_negative(self):
        """Test for a list with all negative numbers."""
        self.assertEqual(max_integer([-6, -50, -75, -1, -100]), -1)

    def test_non_int_arg(self):
        """Test for a non-int type in the list."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Hello", 4, 5])

if __name__ == "__main__":
    unittest.main()
