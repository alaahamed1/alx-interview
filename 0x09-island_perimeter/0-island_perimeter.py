#!/usr/bin/python3
"""island_perimeter module
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == (len(grid) - 1) or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == (len(grid[0]) - 1) or grid[row][col + 1] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
    return perimeter
