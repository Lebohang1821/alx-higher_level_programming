#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.
    """
    return [x % 2 == 0 for x in my_list]
