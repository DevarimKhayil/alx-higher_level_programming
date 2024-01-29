#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    - matrix (list of lists): The input matrix.
    - div (int or float): The divisor.

    Returns:
    A new matrix with each element divided by the divisor.

    Raises:
    - TypeError: If the matrix is not a list of lists or if the rows have different sizes.
    - TypeError: If the matrix elements are not integers or floats.
    - TypeError: If the divisor is not a number.
    - ZeroDivisionError: If the divisor is zero.

    """
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if matrix elements are integers or floats
    if not all(isinstance(value, (int, float)) for row in matrix for value in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element in the matrix by div
    result_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return result_matrix

