#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    # Use list comprehension to create a new matrix
    # Square each element in the sublists of the input matrix
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix
