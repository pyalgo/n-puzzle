def misplaced(grid, n, solved_puzzle):
    h = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != solved_puzzle[i][j]:
                h += 1
    return h


def _linear_conflict(solved_puzzle, unsolved_puzzle):
    conflicts = []

    for solved_row, unsolved_row in zip(solved_puzzle, unsolved_puzzle):
        for i in unsolved_row:
            for j in unsolved_row:
                if j in solved_row and i in solved_row and \
                        (
                                (
                                        solved_row.index(i) != unsolved_row.index(i) and
                                        (
                                                (unsolved_row.index(i) < unsolved_row.index(j) and
                                                 solved_row.index(i) > solved_row.index(j)) or
                                                (
                                                        unsolved_row.index(j) < unsolved_row.index(i) and
                                                        solved_row.index(j) > solved_row.index(i)
                                                )
                                        )
                                ) or (
                                        solved_row.index(j) != unsolved_row.index(j) and
                                        (
                                                (unsolved_row.index(j) < unsolved_row.index(i)
                                                 and solved_row.index(j) > solved_row.index(i))
                                                or
                                                (
                                                        unsolved_row.index(i) < unsolved_row.index(j)
                                                        and
                                                        solved_row.index(i) > solved_row.index(j)
                                                )

                                        )
                                )
                        ):
                    conflicts.append((i, j))
    return conflicts


def linear_conflict_manhattan(grid, n, solved_puzzle):
    horizontal_conflicts = len(_linear_conflict(grid, solved_puzzle))

    vertical_resolved_puzzle = [[] for _ in range(n)]
    vertical_unsolved_puzzle = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            vertical_resolved_puzzle[j].append(solved_puzzle[i][j])
            vertical_unsolved_puzzle[j].append(grid[i][j])

    vertical_conflicts = len(_linear_conflict(vertical_unsolved_puzzle, vertical_resolved_puzzle))

    manhattan_h = manhattan(grid, n, solved_puzzle)

    linear_conflict_h = horizontal_conflicts + vertical_conflicts

    return manhattan_h + linear_conflict_h


def _corner_conflict(grid, n, solved_puzzle):
    conflicts = []

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if grid[i][j] != solved_puzzle[i][j] \
                        and grid[i][j+1] == solved_puzzle[i][j+1] \
                        and grid[i+1][j] == solved_puzzle[i+1][j]:
                    conflicts.append((grid[i][j+1], grid[i+1][j]))
            elif i == 0 and j == n - 1:
                if grid[i][j] != solved_puzzle[i][j] \
                        and grid[i][j - 1] == solved_puzzle[i][j - 1] \
                        and grid[i + 1][j] == solved_puzzle[i + 1][j]:
                    conflicts.append((grid[i][j - 1], grid[i + 1][j]))
            elif i == n-1 and j == n-1:
                if grid[i][j] != solved_puzzle[i][j] \
                        and grid[i][j - 1] == solved_puzzle[i][j - 1] \
                        and grid[i - 1][j] == solved_puzzle[i - 1][j]:
                    conflicts.append((grid[i][j - 1], grid[i - 1][j]))
            elif i == n-1 and j == 0:
                if grid[i][j] != solved_puzzle[i][j] \
                        and grid[i][j + 1] == solved_puzzle[i][j + 1] \
                        and grid[i - 1][j] == solved_puzzle[i - 1][j]:
                    conflicts.append((grid[i][j + 1], grid[i - 1][j]))


def linear_corner_conflict_manhattan(grid, n, solved_puzzle):
    pass

def manhattan(grid, n, solved_puzzle):
    solved = {}
    unsolved = {}

    h = 0
    for i in range(n):
        for j in range(n):
            solved[solved_puzzle[i][j]] = (i, j)
            unsolved[grid[i][j]] = (i, j)

    for num, solved_coors in solved.items():
        unsolved_coors = unsolved[num]
        for c in range(2):
            if unsolved_coors[c] < solved_coors[c]:
                h += solved_coors[c] - unsolved_coors[c]
            else:
                h += unsolved_coors[c] - solved_coors[c]

    return h


