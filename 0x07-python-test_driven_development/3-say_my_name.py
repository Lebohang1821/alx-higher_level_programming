#!/usr/bin/python3
"""It efine name-printing function."""


def say_my_name(first_name, last_name=""):
    """It print name.

    This function takes two arguments, first_name and last_name, and prints them as formatted string.

    Args:
        first_name (str): First name - print.
        last_name (str): Last name - print. (optional, default is an empty string)

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
