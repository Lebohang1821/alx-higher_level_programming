#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=None, idx=0):
    """Delete an item at a specific position in a list."""
    if my_list is None:
        my_list = []

    if 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list
