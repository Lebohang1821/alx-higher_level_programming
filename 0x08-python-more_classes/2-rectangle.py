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
            width (int): The width of the new rectangle (default is 0).
            height (int): The height of the new rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
           It get or set the height of the Rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
           It Set height of Rectangle.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If height is not integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
           It calculate and it returns area of Rectangle.

        Returns:
            int: Area of Rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
           It calculate and it return perimeter of Rectangle.

        Returns:
            int: Perimeter of Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
