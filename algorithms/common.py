def generate_solved_puzzle(m, n):
    k = 0
    l = 0
    val = 1
    res = [[0 for _ in range(m)] for _ in range(m)]

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            res[k][i] = val
            val += 1
        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            res[i][n - 1] = val
            val += 1
        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                res[m - 1][i] = val
                val += 1
            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                res[i][l] = val
                val += 1
            l += 1
    return res

def move_grid(grid, direction):
    """
    moves grid according to the direction
    """
    pass

directions = ['r', 'l', 'd', 'u']