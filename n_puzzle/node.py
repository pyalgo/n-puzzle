from .heuristics import manhattan
from copy import deepcopy


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
