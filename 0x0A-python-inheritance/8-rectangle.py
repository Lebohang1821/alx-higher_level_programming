#!/usr/bin/python3
"""It Defines class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """It represent rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializ ew Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
