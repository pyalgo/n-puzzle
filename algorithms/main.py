#!/usr/bin/env python

from algorithms.common import generate_solved_puzzle


if __name__ == '__main__':
    matrix = [[8,7,5],
              [3,0,1],
              [4,2,6]]
    res = generate_solved_puzzle(5)

    for r in res:
        print(r)
