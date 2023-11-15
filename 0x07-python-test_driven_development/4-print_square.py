#!/usr/bin/python3
"""It should defines square-printing function."""



def print_square(size):
    """It should print square with # character.

    Args:
        size (int): Height/width of square.
        
    Raises:
        TypeError: If the size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
