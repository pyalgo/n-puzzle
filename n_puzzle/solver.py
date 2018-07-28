import sys
from functools import reduce


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
            return
            # sys.exit(0)
        if verbose:
            print(current_node)
        solutions = current_node.get_all_children()
        clean_solutions = list(filter(lambda x: x not in closed_list,
                                      solutions))
        open_list.extend(clean_solutions)
        current_node = reduce(lambda x, y: x if x.F < y.F else y,
                              open_list)
        open_list.remove(current_node)
