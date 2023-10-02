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
        """It initialize new Rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
           Get or set the width of Rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
           It set width of Rectangle.

        Args:
            value (int): Width value to set.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
           It get // set the height of the Rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
           Set height of Rectangle.

        Args:
            value (int): Height value to set.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
           It calculate and it return area of Rectangle.
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
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
           It Return string representation of Rectangle.

        String consists of '#' characters forming shape of Rectangle.

        Returns:
            str: String representation of Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        
        rect = []
        for i in range(self.__height):
            rect.extend(['#' * self.__width])
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
