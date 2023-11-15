#!/usr/bin/python3
"""It define class Square."""


class Square:
    """It represent square."""

    def __init__(self, size=0):
        """It initialize new Square.

        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
