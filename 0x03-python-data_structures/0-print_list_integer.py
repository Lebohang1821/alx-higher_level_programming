#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(_list=None):
    """Print all integers of a list."""
    if _list is None:
        _list = []

    for item in _list:
        print("{:d}".format(item))
