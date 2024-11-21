#!/usr/bin/python3
"""rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """rotate it 90 degrees clockwise.
    """
    for row in matrix:
        row.reverse()
    N = len(matrix)
    for x in range(N - 1):
        for y in range(N - x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N - 1 - y][N - 1 - x]
            matrix[N - 1 - y][N - 1 - x] = temp
