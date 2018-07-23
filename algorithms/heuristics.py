

def manhattan(grid, n, solved_puzzle):
    h = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != solved_puzzle[i][j]:
                h += 1
    return h - 1 if h else 0
