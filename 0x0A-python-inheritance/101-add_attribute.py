#!/usr/bin/python3
"""A function for dynamically adding attributes to objects."""


def add_attribute(obj, attribute_name, attribute_value):
    """Add a new attribute to an object, if possible.

    This function allows - dynamically new attribute with a specified name
    and value - object. It checks if object supports attribute assignment
    and raises a TypeError if it cannot add the attribute.

    Args:
        obj (object): The object to which the attribute will be added.
        attribute_name (str): The name of the attribute to add.
        attribute_value (any): The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute to this object.")
    setattr(obj, attribute_name, attribute_value)
