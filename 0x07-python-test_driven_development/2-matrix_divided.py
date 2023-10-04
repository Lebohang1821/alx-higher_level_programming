#!/usr/bin/python3
"""It defines matrix division function."""


def matrix_divided(matrix, div):
    """It divide all elements of matrix by divisor.

    Args:
        matrix (list): List of integers or floats.
        div (int/float): Divisor.

    Raises:
        TypeError: If matrix is not list of 
        lists containing integers or floats.
        ValueError: If matrix contains rows of different sizes.
        TypeError: If divisor is not int or float.
        ZeroDivisionError: If divisor is 0.

    Returns:
        list: New matrix representing the result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
