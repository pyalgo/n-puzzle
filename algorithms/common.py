def generate_solved_puzzle(matrix_size):
    m = matrix_size
    n = matrix_size
    k = 0
    l = 0
    val = 0
    all_numbers = [i for i in range(1, m*n)]
    all_numbers.append(0)
    res = [[0 for _ in range(m)] for _ in range(m)]

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            res[k][i] = all_numbers[val]
            val += 1
        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            res[i][n - 1] = all_numbers[val]
            val += 1
        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                res[m - 1][i] = all_numbers[val]
                val += 1
            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                res[i][l] = all_numbers[val]
                val += 1
            l += 1
    return res

def move_grid(grid, direction):
    """
    moves grid according to the direction
    """
    for i in range(len(grid)):
        for j in  range(len(grid)):
            if not grid[i][j]:
                if direction == LEFT:
                    pass




    pass

LEFT = 'l'
RIGHT = 'r'
DOWN = 'd'
UP = 'u'

directions = [LEFT, RIGHT, DOWN, UP]