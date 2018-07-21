#!/usr/bin/env python

from algorithms.common import generate_solved_puzzle
from argparse import ArgumentParser
import sys
from .process_input import (remove_comments,
                            parse_input_list,
                            get_size,
                            validate_matrix)

APP_NAME = 'n-puzzle'


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
        print(f'{APP_NAME}: ' + str(e))
        sys.exit(1)
    input_list = remove_comments(raw_input)
    matrix = parse_input_list(input_list)
    size = get_size(matrix.pop(0))
    validate_matrix(matrix, size)
    # matrix = [[8,7,5],
    #           [3,0,1],
    #           [4,2,6]]
    # res = generate_solved_puzzle(5)
    # for r in res:
    #     print(r)
