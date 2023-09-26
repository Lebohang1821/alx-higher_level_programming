#!/usr/bin/python3
"""It define class Square."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """It initialize new square.

        Args:
            size (int): Size of new square.
            position (tuple): Psition of new square as a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """It get or set size of square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """It get or set position of square.

        Raises:
            TypeError: If the position is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """It calculate and return area of square.

        Returns:
            int: Area of square.
        """
        return self.__size * self.__size

    def my_print(self):
        """It Print square using '#' characters, considering position.

        If size is equal - 0, print a empty line.
        Position is used to insert spaces accordingly when position[1] > 0.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
