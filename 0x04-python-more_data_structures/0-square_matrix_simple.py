#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _new_matrix = matrix.copy()

    for i in range(len(matrix)):
        _new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return _new_matrix
