# pylint: disable=missing-docstring

def sudoku_validator(grid):

    # process rows

    for block in grid:  # single loop --> 1 dimension
        if set(block) != {1,2,3,4,5,6,7,8,9}:
            return False
    
    # process columns

    for i in range(9):  # double loop with variables i, j --> 2 dimension
        test = []
        for j in range(9):
            test.append(grid[j][i])

        if set(test) != {1,2,3,4,5,6,7,8,9}:
            return False
    
    # process mini-grid

    seg = [list(zip(*(iter(row),) * 3)) for row in grid]
    seg = list(zip(*(iter(seg),) * 3))

    for i in range(3):  # triple loop with variables i, j, k --> 3 dimension
        for j in range(3):
            test = []
            for k in range(3):
                test += list(seg[j][k][i])

            if set(test) != {1,2,3,4,5,6,7,8,9}:
                return False

    return True
