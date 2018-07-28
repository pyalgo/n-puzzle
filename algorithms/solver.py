import sys
from functools import reduce
from .node import Node


def print_report(node: Node, complexity_in_time):
    deepness = 0
    solution_sequence = []
    while node is not None:
        solution_sequence.append(node)
        deepness += 1
        node = node.parent
    print('The ordered sequence of states that make up the solution')
    print(f'Total number of states ever selected in the "opened" set'
          f' (complexity in time): {complexity_in_time}')
    print(f'Minimum number of moves required to reach the solution:'
          f' {deepness}')


def solve(current_node, verbose=False):
    open_list = [current_node, ]
    closed_list = []
    complexity_in_time = 0
    complexity_in_size = 0
    i = 0
    while open_list:
        complexity_in_time += 1
        open_list.remove(current_node)
        closed_list.append(current_node)
        if current_node.is_solved:
            print('Solution Found!')
            print_report(current_node, complexity_in_time)
            print(current_node)
            sys.exit(0)
        if verbose:
            print(current_node)
        solutions = current_node.get_all_children()
        clean_solutions = list(filter(lambda x: x not in closed_list,
                                      solutions))
        open_list.extend(clean_solutions)
        current_node = reduce(lambda x, y: x if x.F < y.F else y,
                              open_list)
    print('Solution does not exist')
    sys.exit(0)
