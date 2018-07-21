from io import StringIO
import re
import sys

APP_NAME = 'n-puzzle'


def remove_comments(raw_input):
    res = []
    for line in StringIO(raw_input):
        line = line.strip()
        if '#' in line:
            res.append(re.search('(.*)#', line).groups()[0])
        else:
            res.append(line)
    return list(filter(None, res))


def parse_input_list(input_list):
    matrix = []
    for line in input_list:
        try:
            matrix.append(list(map(lambda x: int(x), line.split())))
        except ValueError:
            print(f'{APP_NAME}: error: invalid numbers format')
            sys.exit(1)
    return matrix


def get_size(size_row):
    try:
        if len(size_row) != 1:
            raise IndexError
        size = int(size_row[0])
    except (IndexError, ValueError) as e:
        print(f'{APP_NAME}: error: invalid puzzle size format')
        sys.exit(1)
    return size


def _validate_size(matrix, size):
    if len(matrix) != size or list(filter(lambda x: len(x) != size, matrix)):
        print(f'{APP_NAME}: error: invalid puzzle size')
        sys.exit(1)


def _validate_numbers(matrix, size):
    all_numbers = []
    for row in matrix:
        all_numbers.extend(row)
    all_numbers = set(all_numbers)
    valid_numbers = set(range(size ** 2))
    if all_numbers != valid_numbers:
        print(f'{APP_NAME}: error: invalid puzzle numbers')
        sys.exit(1)


def validate_matrix(matrix, size):
    _validate_size(matrix, size)
    _validate_numbers(matrix, size)


def _get_inversions_count(tiles, size):
    count = 0
    for i in range(size ** 2 - 1):
        for j in range(i, size ** 2):
            if tiles[i] and tiles[j] and tiles[i] > tiles[j]:
                count += 1
    return count


def _solvable_if_odd(inversions):
    if inversions % 2 == 0:
        print('The puzzle is solvable')
    else:
        print('The puzzle is not solvable. exiting')
        sys.exit(0)


def _get_blank_row(matrix, size):
    for i, row in reversed(list(enumerate(matrix))):
        if 0 in row:
            return size - i


def _solvable_if_even(size, inversions, matrix):
    blank_row = _get_blank_row(matrix, size)
    if blank_row % 2 == 0 and inversions % 2 != 0:
        print('The puzzle is solvable')
    elif blank_row % 2 != 0 and inversions % 2 == 0:
        print('The puzzle is solvable')
    else:
        print('The puzzle is not solvable. exiting')
        sys.exit(0)


def check_if_solvable(matrix, size):
    tiles = []
    for row in matrix:
        tiles.extend(row)
    inversions = _get_inversions_count(tiles, size)
    if size % 2 == 0:
        _solvable_if_even(size, inversions, matrix)
    else:
        _solvable_if_odd(inversions)


if __name__ == '__main__':
    s = '''#This puzzle is unsolvable
    4
    9 15 13 1 
    2 12 11 5 
    14 4 10 0 
    3 6 7 8 
    '''
    input_list = remove_comments(s)
    matrix = parse_input_list(input_list)
    size = get_size(matrix.pop(0))
    validate_matrix(matrix, size)
    check_if_solvable(matrix, size)
    # for line in matrix:
    #     print(line)
