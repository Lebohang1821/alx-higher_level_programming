#!/usr/bin/python3
"""It define class Square."""


class Square:
    """It represent square."""

    def __init__(self, size=0):
        """It initialize new square.

        Args:
            size (int): Size of new square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """It get curent size of square."""
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
        return self.__size * self.__size

    def my_print(self):
        """Print square with # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
