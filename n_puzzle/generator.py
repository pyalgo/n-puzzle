import random
from n_puzzle.process_input import check_if_solvable

def make_puzzle(s, solvable, iterations):
    def swap_empty(p):
        idx = p.index(0)
        poss = []
        if idx % s > 0:
            poss.append(idx - 1)
        if idx % s < s - 1:
            poss.append(idx + 1)
        if idx / s > 0:
            poss.append(idx - s)
        if idx / s < s - 1:
            poss.append(idx + s)
        swi = random.choice(poss)
        p[idx] = p[swi]
        p[swi] = 0

    p = make_goal(s)
    for i in range(iterations):
        swap_empty(p)

    if not solvable:
        if p[0] == 0 or p[1] == 0:
            p[-1], p[-2] = p[-2], p[-1]
        else:
            p[0], p[1] = p[1], p[0]
    return p


def make_goal(s):
    ts = s * s
    puzzle = [-1 for i in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        puzzle[x + y * s] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y * s] != -1):
            iy = ix
            ix = 0
        elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y + iy) * s] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == s * s:
            cur = 0

    return puzzle


def generate_puzzle(s=3, solvable=True, iterations=100):
    random.seed()
    puzzle = make_puzzle(s, solvable=solvable, iterations=iterations)
    p = "#This puzzle is %s\n" % ("solvable" if solvable else "unsolvable")
    p += "%d\n" % s
    for i in range(s):
        for j in range(s):
            p += str(puzzle[j + i * s]) + ' '
        p += '\n'

    res = [[0 for _ in range(s)] for _ in range(s)]

    count = 0
    for i in range(s):
        for j in range(s):
            res[i][j] = puzzle[count]
            count +=1

    print(p.strip())
    check_if_solvable(res, size=s)
    return p.strip()


print(generate_puzzle())
