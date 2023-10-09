#!/usr/bin/python3
"""Custom list class MyList that extends functionality of built-in list"""

class MyList(list):
    """
    A custom list class that inherits from built-in list class and adds
    the ability to print its elements in sorted ascending order.
    """

    def print_sorted(self):
        """
        Print the elements of list in sorted ascending order.
        """
        print(sorted(self))
