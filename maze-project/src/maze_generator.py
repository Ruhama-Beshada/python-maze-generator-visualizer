import random
from renderer import northWall, eastWall
from constants import *

visited = set()
stack = []


def remove_wall(a, b):

    r1, c1 = a
    r2, c2 = b

    if c2 == c1 + 1:      # RIGHT
        eastWall[r1][c2] = 0

    elif c2 == c1 - 1:    # LEFT
        eastWall[r1][c1] = 0

    elif r2 == r1 + 1:    # DOWN
        northWall[r2][c2] = 0

    elif r2 == r1 - 1:    # UP
        northWall[r1][c1] = 0


def get_neighbors(cell):

    r, c = cell

    directions = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]

    result = []

    for nr, nc in directions:
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if (nr, nc) not in visited:
                result.append((nr, nc))

    return result


def generate_maze():

    start = (0, 0)

    stack.append(start)
    visited.add(start)

    while stack:

        current = stack[-1]

        neighbors = get_neighbors(current)

        if neighbors:
            nxt = random.choice(neighbors)
            remove_wall(current, nxt)
            visited.add(nxt)
            stack.append(nxt)

        else:
            stack.pop()

    # 🚪 FIXED ENTRANCE / EXIT

    # TOP-LEFT OPEN
    eastWall[0][0] = 0

    # BOTTOM-RIGHT OPEN
    eastWall[ROWS - 1][COLS] = 0