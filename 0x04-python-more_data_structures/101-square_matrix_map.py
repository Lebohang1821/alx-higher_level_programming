#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda y: y**2, x)) for x in matrix]
