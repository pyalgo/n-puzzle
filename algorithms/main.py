#!/usr/bin/env python

from algorithms.common import generate_solved_puzzle, move_grid, LEFT, RIGHT, DOWN, UP, directions, print_matrix
from algorithms.Manhattan import manhattan_district, count_manhattan_h
from algorithms.node import Node




if __name__ == '__main__':
    matrix = [[1, 8, 5],
              [6, 0, 2],
              [7, 4, 3]]
    print_matrix(matrix)
    # while True:
    #     dir = input()
    #     if any(d == dir for d in directions):
    #         matrix = move_grid(matrix, dir)
    #         print_matrix(matrix)

    first_node = Node(grid=matrix)
    first_node.G = 0
    first_node.H = count_manhattan_h(matrix)
    first_node.F = first_node.H + first_node.G
    full_path = manhattan_district(first_node, [])
    last_node = full_path[len(full_path) - 1]
    # print_matrix(last_node.grid)
