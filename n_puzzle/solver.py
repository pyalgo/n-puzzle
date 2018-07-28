import sys
from .node import Node
import heapq
from time import time


def print_report(node: Node, show_solution, complex_in_time,
                 complex_in_size, start_time):
    deepness = 0
    solution_sequence = []
    current_node = node
    while current_node is not None:
        solution_sequence.append(current_node)
        deepness += 1
        current_node = current_node.parent
    if show_solution:
        print('Moves that make up a solution:')
        for item in reversed(solution_sequence):
            print(item)
    print('Solution is:')
    print(node)
    print(f'Complexity in time: {complex_in_time}')
    print(f'Complexity in size: {complex_in_size}')
    print(f'Number of moves to solution: {deepness}')
    print(f'Execution time: {round(time() - start_time, 3)} ms')


def solve(current_node, start_time, verbose=False, solution_sequence=False):
    open_set = []
    heapq.heappush(open_set, (current_node.F, current_node))
    closed_set = {}
    complex_in_time = 0
    complex_in_size = 0
    while open_set:
        current_node = heapq.heappop(open_set)[1]
        complex_in_time += 1
        closed_set[(str(current_node.grid))] = None
        if current_node.is_solved:
            print_report(current_node, solution_sequence, complex_in_time,
                         complex_in_size, start_time)
            sys.exit(0)
        if verbose:
            print(current_node)
        solutions = current_node.get_all_children()
        clean_solutions = list(filter(lambda x: str(x.grid) not in closed_set,
                                      solutions))
        complex_in_size += len(clean_solutions)
        for candidate in clean_solutions:
            heapq.heappush(open_set, (candidate.F, candidate))
    print('Solution does not exist')
    sys.exit(0)
