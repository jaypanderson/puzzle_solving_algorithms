"""
algorithm that solves the 16 diagonals problem. there is a board with five rows and 5 columns with a total of 25 cells.
The goal is to place 16 diagonal lines that go from the corner of a cell to the opposite corner.  But the edges of these
diagonals must not touch others edges from other cells.  This algorithm gives the following solution.

[[1, 1, 1, 0, 2],
 [0, 0, 1, 0, 2],
 [2, 2, 0, 2, 2],
 [2, 0, 1, 0, 0],
 [2, 0, 1, 1, 1]]

The 0s represent empty cells, the 1s represent a '/' (lower left to upper right (slash)) and 2s represent a '\'
(upper left to lower right (backslash)).  So if we convert it it looks something like this.

[[/, /, /, 0, \],
 [0, 0, /, 0, \],
 [\, \, 0, \, \],
 [\, 0, /, 0, 0],
 [\, 0, /, /, /]]

if we move the formating it looks more like this

 / / /   \
     /   \
 \ \   \ \
 \   /
 \   / / /

"""

def can_extend(perm, i, j, direc, n):
    ul_lr = [[-1, -1], [1, 1]]
    ur_ll = [[-1, 1], [1, -1]]
    sides = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    if n < 0:
        return False
    elif direc == 1:
        for y, x in ur_ll:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 1:
                return False
        for y, x in sides:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 2:
                return False
    else:
        for y, x in ul_lr:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 2:
                return False
        for y, x in sides:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 1:
                return False

    return True


def extend(perm: list, n: int, rows: int, cols: int, seen: set):
    config_str = ''.join(''.join(str(cell) for cell in row) for row in perm)
    if config_str in seen:
        return False

    if n == 0:
        print("success: ", perm)
        print(len(seen))
        return True

    seen.add(config_str)

    for i in range(rows):
        for j in range(cols):
            if perm[i][j] == 0:
                for direc in range(1, 3):
                    perm[i][j] = direc
                    if can_extend(perm, i, j, direc, n - 1):
                        print(perm)
                        if extend(perm, n - 1, rows, cols, seen):
                            #print("test")
                            return True
                    perm[i][j] = 0
    return False

perm = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


extend(perm, 16, 5, 5, set())
