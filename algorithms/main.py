#!/usr/bin/env python

from pprint import pprint
from algorithms.graph import Graph


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



if __name__ == '__main__':
    # raw_graph = {
    #     4: [1, 5],
    #     1: [4, 2, 7],
    #     2: [1, 3],
    #     5: [4, 7, 8],
    #     7: [1, 3, 5, 6],
    #     3: [2, 7, 0],
    #     8: [5, 6],
    #     6: [8, 7, 0],
    #     0: [6, 3]
    # }
    # g = Graph(raw_graph)
    # pprint(g)
    matrix = [[8,7,5],
              [3,0,1],
              [4,2,6]]
    print(generate_solved_puzzle(3, 3))



