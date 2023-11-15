#!/usr/bin/python3
"""It defines class-to-JSON function."""


def class_to_json(obj):
    """It return dictionary represntation of simple data structure."""
    return obj.__dict__
