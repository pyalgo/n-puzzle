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


if __name__ == '__main__':
    s = '''#This puzzle is solvable
    3
    4 8 1 #fuck
    #sdfsd
    7 3 6
    5 2 0
    '''
    input_list = remove_comments(s)
    matrix = parse_input_list(input_list)
    size = get_size(matrix.pop(0))
    validate_matrix(matrix, size)
    for line in matrix:
        print(line)
