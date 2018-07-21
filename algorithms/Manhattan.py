from algorithms.common import generate_solved_puzzle,generate_solved_puzzle_test, directions, move_grid, print_matrix
from algorithms.node import Node
from copy import deepcopy


def count_manhattan_h(grid):
    h_count = 0
    solved_puzzle = generate_solved_puzzle(len(grid))
    for i in range(len(grid)):
        for j in range(len(grid)):
            if not grid[i][j] is solved_puzzle[i][j] and grid[i][j] and solved_puzzle[i][j]:
                h_count += 1

    return h_count


def get_all_grids(full_path):
    return [n.grid for n in full_path]


def get_best_child(parent_node, full_path):
    best_child = None
    for d in directions:
        parent_grid = deepcopy(parent_node.grid)
        new_grid = move_grid(parent_grid, d)
        new_child = Node(grid=new_grid)
        new_child.G = parent_node.G + 1
        new_child.H = count_manhattan_h(new_child.grid)
        new_child.F = new_child.G + new_child.H
        if not best_child and new_grid != parent_node.grid and not new_grid in get_all_grids(full_path):
            best_child = new_child
        if best_child and  new_child.F < best_child.F:
            if new_grid != parent_node.grid and not new_grid in get_all_grids(full_path):
                best_child = new_child
    return best_child


def manhattan_district(parent_node, full_path):
    # full_path.append(parent_node)
    # print_matrix(parent_node.grid)
    # best_child = get_best_child(parent_node, full_path)
    # if best_child.grid != generate_solved_puzzle(len(best_child.grid)):
    #     return manhattan_district(best_child, full_path)
    # else:
    #     print_matrix(best_child.grid)
    #     full_path.append(best_child)
    #     return full_path

    while True:
        full_path.append(parent_node)
        best_child = get_best_child(parent_node, full_path)
        print_matrix(best_child.grid)
        parent_node = best_child
        if best_child.grid is generate_solved_puzzle(len(best_child.grid)):
            return full_path
