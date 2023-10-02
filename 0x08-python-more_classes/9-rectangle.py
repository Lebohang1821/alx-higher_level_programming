#!/usr/bin/python3
"""It Defines Rectangle class."""


class Rectangle:
    """It Represent rectangle.

    Attributes:
        instances (int): Number of Rectangle instances.
        symbol (any): Symbol used for string representation.
    """

    instances = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """It initialize new Rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        type(self).instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """It get/set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): First Rectangle.
            rect_2 (Rectangle): Second Rectangle.
        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): Width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the symbol character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).instances -= 1
        print("Bye rectangle...")
