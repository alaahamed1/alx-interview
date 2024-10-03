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
        trangle = []
        for i in range(n):
            if i == 0:
                trangle.append([1])
            elif i == 1:
                trangle.append([1, 1])
            else:
                row = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        row.append(1)
                    else:
                        row.append(trangle[i - 1][j - 1] + trangle[i - 1][j])
                trangle.append(row)
    return trangle
