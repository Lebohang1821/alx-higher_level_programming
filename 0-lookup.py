#!/usr/bin/python3
"""
Object Attribute Lookup Function
"""

def lookup(obj):
    """
    Get list of attributes of an object.

    Args:
        obj (object): The Python object for which attributes are to be retrieved.

    Returns:
        list: A list containing the names of all attributes associated with the object.
    """
    # Use the 'dir()' function to obtain a list of attributes for the given object.
    return (dir(obj))
