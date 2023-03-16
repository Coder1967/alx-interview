#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty
"""


def rotate_2d_matrix(matrix) -> None:
    """
    function to handle the rotation
    Return: None
    """
    height: int = len(matrix)
    width: int = len(matrix[0])
    matrix_copy = matrix[:]
    matrix.clear()

    for i in range(width):
        j: int = height - 1
        new_list = []
        while j >= 0:
            new_list.append(matrix_copy[j][i])
            j -= 1
        matrix.append(new_list)
