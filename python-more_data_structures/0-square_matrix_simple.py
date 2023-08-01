#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        inside_matrix = []
        for i in row:
            square = i**2
            inside_matrix.append(square)
        new_matrix.append(inside_matrix)
    return(new_matrix)
