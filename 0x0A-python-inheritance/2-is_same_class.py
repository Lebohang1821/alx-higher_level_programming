#!/usr/bin/python3
"""Defines function to check if an object is instance of specific class"""


def is_instance_of_class(obj, class_to_check):
    """Check if an object is instance of particular class

    Args:
        obj (any): Object to be checked.
        class_to_check (type): Class to compare object's type with

    Returns:
        bool: True if object is instance of specified class, False otherwise
    """
    if type(obj) == class_to_check:
        return (True)
    return (False)
