#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """
    if n <= 0:
        return []
    if type(n) is int:
        triangle = []
        for i in range(n):
            if i == 0:
                triangle.append([1])
            else:
                row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
                triangle.append(row)
        return triangle
