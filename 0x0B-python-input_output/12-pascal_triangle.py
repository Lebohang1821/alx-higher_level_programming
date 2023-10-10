#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""

def generate_pascals_triangle(n):
    """Generate Pascal's Triangle up to a given row.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle with 'n' rows.
            Each inner list represents a row in the triangle, containing integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        current_row = triangle[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
