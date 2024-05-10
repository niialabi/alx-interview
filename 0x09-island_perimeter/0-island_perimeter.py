#!/usr/bin/python3
""" island peremeter function  """


def island_perimeter(grid):
    """ Finds perimeter of the island """
    m, n = len(grid), len(grid[0])
    perimeter = 0
    visited = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                perimeter += 4
                if (i - 1, j) in visited:
                    perimeter -= 2
                if (i + 1, j) in visited:
                    perimeter -= 2
                if (i, j - 1) in visited:
                    perimeter -= 2
                if (i, j + 1) in visited:
                    perimeter -= 2
                visited.add((i, j))

    return perimeter
