#!/usr/bin/python3
'''A unittest module for testing the max_integer function.
'''
import unittest
from importlib import import_module

class TestMaxInteger(unittest.TestCase):
    '''Tests the max_integer function.
    '''
    def test_max_integer(self):
        '''Test cases for the max_integer function.
        '''
        # Test an empty list, the result should be None
        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)

        # Test a list with a single element, the result should be that element
        self.assertEqual(max_integer([5]), 5)

        # Test a list with positive and negative integers
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)

        # Test a list with positive integers only
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)

        # Test a list with negative integers only
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)

        # Test a list with both positive and negative integers
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)

        # Test a list with positive and negative integers, including zero
        self.assertEqual(max_integer([7, 1, -18, -6]), 7)

        # Test a list with positive integers and a positive maximum
        self.assertEqual(max_integer([-7, 1, -18, 9]), 9)

if __name__ == '__main__':
    unittest.main()
