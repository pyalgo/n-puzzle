#!/usr/bin/env python

from algorithms.common import generate_solved_puzzle, move_grid, LEFT, RIGHT, DOWN, UP, directions, print_matrix
from algorithms.Manhattan import manhattan_district, count_manhattan_h
from algorithms.node import Node
from argparse import ArgumentParser
import sys
from .process_input import (remove_comments,
                            parse_input_list,
                            get_size,
                            validate_matrix,
                            check_if_solvable)
from .solver import (Node, recursive_solve)

# sys.setrecursionlimit(100000)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='path to the input file')
    parser.add_argument('-f', default='manhattan',
                        help='heuristic function. "manhattan-distance"'
                             ' by default')
    args = parser.parse_args()
    try:
        with open(args.file_path, 'r') as f:
            raw_input = f.read()
    except FileNotFoundError as e:
        print('n-puzzle: ' + str(e))
        sys.exit(1)
    input_list = remove_comments(raw_input)
    matrix = parse_input_list(input_list)
    size = get_size(matrix.pop(0))
    validate_matrix(matrix, size)
    check_if_solvable(matrix, size)

    solved = generate_solved_puzzle(3)
    node = Node(matrix, size, 0, solved)
    node.evaluate()
    recursive_solve(node)

    # matrix = [[1, 2, 3],
    #           [0, 8, 4],
    #           [7, 6, 5]]
    # node = Node(matrix)
    #
    # graph = {
    #     node: None
    # }
    #
    # print(node)
    # print_matrix(matrix)
    # while True:
    #     dir = input()
    #     if any(d == dir for d in directions):
    #         matrix = move_grid(matrix, dir)
    #         print_matrix(matrix)

    # first_node = Node(grid=matrix)
    # first_node.G = 0
    # first_node.H = count_manhattan_h(matrix)
    # first_node.F = first_node.H + first_node.G
    # full_path = manhattan_district(first_node, [])
    # last_node = full_path[len(full_path) - 1]
    # print_matrix(last_node.grid)

