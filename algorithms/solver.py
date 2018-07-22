from .common import generate_solved_puzzle
from copy import deepcopy
import sys
from functools import reduce


def manhattan(grid, n, solved_puzzle):
    h = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != solved_puzzle[i][j]:
                h += 1
    return h - 1 if h else 0


class Node:

    def __init__(self, parent, grid, n, g, solved_puzzle,
                 heuristic=manhattan):
        self.parent = parent
        self.grid = grid
        self.n = n
        self.solved_puzzle = solved_puzzle
        self.H = 0
        self.G = g
        self.F = 0
        self.heuristic = heuristic
        self.zero_x = 0
        self.zero_y = 0

    def __repr__(self):
        s = ''
        for row in self.grid:
            s += str(row) + '\n'
        s += f'G={self.G}\n'
        s += f'H={self.H}\n'
        s += f'F={self.F}\n'
        return s

    def __eq__(self, other):
        return self.grid == other.grid

    @property
    def is_solved(self):
        return True if self.grid == self.solved_puzzle else False

    def evaluate(self):
        self.H = self.heuristic(self.grid, self.n, self.solved_puzzle)
        self.F = self.H + self.G
        self._define_zero_coords()

    def _define_zero_coords(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    self.zero_x = i
                    self.zero_y = j
                    return i, j

    def _swap(self, target_x, target_y):
        target_value = self.grid[target_x][target_y]
        new_grid = deepcopy(self.grid)
        new_grid[self.zero_x][self.zero_y] = target_value
        new_grid[target_x][target_y] = 0
        return new_grid

    def _initiate_node(self, x, y):
        new_grid = self._swap(x, y)
        node = Node(self, new_grid, self.n, self.G + 1,
                    self.solved_puzzle, self.heuristic)
        node.evaluate()
        return node

    def get_all_children(self):
        children = []
        if self.zero_x != 0:
            children.append(self._initiate_node(self.zero_x - 1, self.zero_y))
        if self.zero_x != self.n - 1:
            children.append(self._initiate_node(self.zero_x + 1, self.zero_y))
        if self.zero_y != 0:
            children.append(self._initiate_node(self.zero_x, self.zero_y - 1))
        if self.zero_y != self.n - 1:
            children.append(self._initiate_node(self.zero_x, self.zero_y + 1))
        return children


def solve(current_node, verbose=False):
    open_list = []
    closed_list = []
    i = 0
    while True:
        i += 1
        closed_list.append(current_node)
        if current_node.is_solved:
            print('Solution Found!')
            print(current_node)
            sys.exit(0)
        if verbose:
            print(current_node)
        solutions = current_node.get_all_children()
        clean_solutions = list(filter(lambda x: x not in closed_list, solutions))
        open_list.extend(clean_solutions)
        current_node = reduce(lambda x, y: x if x.F < y.F else y,
                              open_list)
        open_list.remove(current_node)


if __name__ == '__main__':
    matrix = [[1, 2, 0],
              [7, 8, 3],
              [6, 5, 4]]

    matrix = [[0, 6, 5],
              [7, 3, 1],
              [2, 4, 8]]

    n = 3
    solved = generate_solved_puzzle(3)
    node = Node(None, matrix, n, 0, solved, manhattan)
    node.evaluate()
    solve(node)
