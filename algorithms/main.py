#!/usr/bin/env python

from algorithms.common import generate_solved_puzzle
from argparse import ArgumentParser
import sys
from .process_input import (remove_comments,
                            parse_input_list,
                            get_size,
                            validate_matrix,
                            check_if_solvable)
from .solver import solve
from .node import Node
from .heuristics import manhattan


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='path to the input file')
    parser.add_argument('-f', default='manhattan',
                        help='heuristic function. "manhattan-distance"'
                             ' by default')
    parser.add_argument('-v', action='store_true', default=False,
                        help='verbose')
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

    heuristics = {
        'manhattan': manhattan
    }

    solved = generate_solved_puzzle(size,)
    node = Node(None, matrix, size, 0, solved, heuristic=heuristics[args.f])
    node.evaluate()
    solve(node, verbose=args.v)
