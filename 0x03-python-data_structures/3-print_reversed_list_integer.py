#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.
    """
    if isinstance(my_list, list):
        my_list.reverse()
        [print("{:d}".format(i)) for i in my_list if isinstance(i, int)]
