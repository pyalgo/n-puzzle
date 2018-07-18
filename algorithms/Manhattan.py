from .common import generate_solved_puzzle, directions, move_grid
from .node import Node


def count_manhattan_h(grid):
    pass


def get_best_child(parent_node):
    parent_grid = parent_node.grid
    best_child = None
    for d in directions:
        new_child = Node(grid=move_grid(parent_grid, d))
        new_child.G = parent_node.G + 1
        new_child.H = count_manhattan_h(new_child.grid)
        new_child.F = new_child.G + new_child.F
        if best_child:
            if new_child.F < best_child.F:
                best_child = new_child
        else:
            best_child = new_child
    return best_child


def manhattan_district(parent_node, full_path):
    full_path.append(parent_node)
    best_child = get_best_child(parent_node)
    if not best_child.grid is generate_solved_puzzle(len(best_child.grid), len(best_child.grid)):
        return manhattan_district(best_child, full_path)
    else:
        return full_path
