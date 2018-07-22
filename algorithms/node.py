

class Node:

    def __init__(self, grid):
        self.grid = grid
        self.H = None
        self.G = None
        self.F = None

    def __repr__(self):
        s = ''
        for row in self.grid:
            s += str(row) + '\n'
        return s.strip()

    def evaluate_node(self):
        pass

