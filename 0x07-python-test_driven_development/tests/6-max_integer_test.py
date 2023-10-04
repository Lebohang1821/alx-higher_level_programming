#!/usr/bin/python3
'''A unittest module for the max_integer function.
'''
import unittest
from importlib import import_module


class TestMaxInteger(unittest.TestCase):
    '''Tests the max_integer function.
    '''
    def test_area(self):
        '''The equality tests for the max_integer function.
        '''
        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)
        self.assertEqual(max_integer([7, 1, -18, -6]), 7)
        self.assertEqual(max_integer([-7, 1, -18, 9]), 9)
