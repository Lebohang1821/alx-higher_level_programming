#!/usr/bin/python3
"""It defines Rectangle class."""


class Rectangle:
    """
       It represent rectangle.

    Attributes:
        width (int): Width of rectangle.
        height (int): Height of rectangle.
    """

    def __init__(self, width=0, height=0):
        """
           It initialize new Rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width o rectangle.

        Raises:
            TypeError: If width is not integer.
            ValueError: If width is less than 0.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """It get // set height of rectangle.

        Raises:
            TypeError: If height is not integer.
            ValueError: If height is less than 0.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
