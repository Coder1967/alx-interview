#!/usr/bin/python3
"""alx question to train for interviews.
"""


def island_perimeter(grid):
    """check the readme for task details.
    """
    if grid is None or len(grid) == 0:
        return 0

    height: int = 0
    width: int = 0
    check = {}
    check['col'] = -10
    i = 0

    while i < len(grid):
        j = 0
        check['row'] = i
        while j < len(grid[0]):
            if grid[i][j] == 1 and check['row'] == i:
                width += 1
            if grid[i][j] == 1 and check['col'] == -10:
                check['col'] = j
            if grid[i][j] == 1 and check['col'] == j:
                height += 1
            j += 1
        i += 1
        if width == 1:
            width = 0
    return 2 * (width + height)
