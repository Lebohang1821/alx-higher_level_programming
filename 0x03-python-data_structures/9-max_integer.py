#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=None):
    """
    Find the biggest integer of a list.
    """
    if my_list is None:
        return None

    if not my_list:
        return None

    biggest = my_list[0]

    for item in my_list:
        if item > biggest:
            biggest = item

    return biggest
