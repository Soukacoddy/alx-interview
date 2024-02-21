#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix 90 degrees clockwise"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            holder = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = holder
    for i in range(n):
        matrix[i].reverse()
