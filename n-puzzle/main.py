#!/usr/bin/env python

from .common import generate_solved_puzzle
from argparse import ArgumentParser
import sys
from .process_input import (remove_comments,
                            parse_input_list,
                            get_size,
                            validate_matrix,
                            check_if_solvable)
from .solver import solve
from .node import Node

from .heuristics import (manhattan, misplaced, linear_conflict_manhattan)
from .generator import generate_puzzle
from .common import print_matrix


if __name__ == '__main__' and __package__:
    parser = ArgumentParser()
    parser.add_argument('-f', metavar='file_path',
                        help='path to the input file')
    parser.add_argument('-hr', metavar='heuristic', default='manhattan',
                        help='heuristic function. "manhattan-distance"'
                             ' by default')
    parser.add_argument('-v', action='store_true', default=False,
                        help='Verbose. Show all visited options')
    parser.add_argument('-p', action='store_true', default=False,
                        help='Show solution path')
    parser.add_argument('-s', metavar='size', type=int,
                        help='specify puzzle size')
    args = parser.parse_args()
    if args.f and args.s:
        print('Both of the -f -s are specify. Exiting')
        sys.exit(0)
    if (args.s and args.s < 2) or args.s == 0:
        print('Puzzle size should be >= 2. Exiting')
        sys.exit(0)
    if args.f:
        try:
            with open(args.f, 'r') as f:
                raw_input = f.read()
        except FileNotFoundError as e:
            print('n-puzzle: ' + str(e))
            sys.exit(1)
    else:
        raw_input = generate_puzzle(size=args.s)
    input_list = remove_comments(raw_input)
    matrix = parse_input_list(input_list)
    size = get_size(matrix.pop(0))
    print('Input puzzle is:')
    print_matrix(matrix)
    validate_matrix(matrix, size)
    check_if_solvable(matrix, size)

    heuristics = {
        'misplaced': misplaced,
        'manhattan': manhattan,
        'linear_conflict_manhattan': linear_conflict_manhattan
    }

    solved = generate_solved_puzzle(size,)
    node = Node(None, matrix, size, 0, solved, heuristic=heuristics[args.hr])
    node.evaluate()
    solve(node, verbose=args.v, solution_sequence=args.p)
