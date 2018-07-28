from .common import generate_solved_puzzle
import random


def _define_zero_coords(p, s):
    for i in range(s):
        for j in range(s):
            if p[i][j] == 0:
                return i, j


def swap(p, size):
    zero_x, zero_y = _define_zero_coords(p, size)
    options = []
    if zero_x != 0:
        options.append((zero_x - 1, zero_y))
    if zero_x != size - 1:
        options.append((zero_x + 1, zero_y))
    if zero_y != 0:
        options.append((zero_x, zero_y - 1))
    if zero_y != size - 1:
        options.append((zero_x, zero_y + 1))
    swap_x, swap_y = random.choice(options)
    p[zero_x][zero_y] = p[swap_x][swap_y]
    p[swap_x][swap_y] = 0


def _stringify_puzzle(p, s):
    s = f'{s}\n'
    for row in p:
        for item in row:
            s += str(item) + ' '
        s += '\n'
    return s.strip()


def generate_puzzle(size=3, iterations=1000):
    random.seed()
    p = generate_solved_puzzle(size)
    for i in range(iterations):
        swap(p, size)
    return _stringify_puzzle(p, size)


if __name__ == '__main__':
    p = generate_puzzle(3)
    print(p)
