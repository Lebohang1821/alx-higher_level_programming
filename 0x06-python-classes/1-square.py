#!/usr/bin/python3
"""It Define class Square."""


class Square:
    """It represent square."""

    def __init__(self, size):
        """It initialize new Square.

        Args:
            size (int): Size of the new square.
        """
        self.__size = size

    def get_size(self):
        """It get size of the square."""
        return self.__size

    def set_size(self, size):
        """It et the size of the square."""
        self.__size = size
