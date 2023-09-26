#!/usr/bin/python3
"""It define class Square."""


class Square:
    """It represent square."""

    def __init__(self, size=0):
        """It initialize new square.

        Args:
            size (int): Size of new square.
        """
        self.size = size

    @property
    def size(self):
        """It get current size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return self.__size ** 2  # Use ** to calculate the square

    def __str__(self):
        """Return string representation of square."""
        return f"Square with size: {self.size}"
