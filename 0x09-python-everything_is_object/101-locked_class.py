#!/usr/bin/python3
"""It defines restricted attribute class."""


class LockedClass:
    """
    It restricts creation of new attributes for instances of this class
    to only allow 'first_name' attribute.
    """

    __slots__ = ["first_name"]
