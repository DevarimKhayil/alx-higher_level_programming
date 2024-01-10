#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the matrix
    for row in matrix:
        new_row = []  # Create a new row for the new matrix
        # Iterate through each element in the row, square it, and append to the new row
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)  # Append the new row to the new matrix

    return new_matrix
