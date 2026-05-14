import random
from constants import *
from renderer import northWall, eastWall


def generate_maze():

    stack = []
    visited = set()

    current = (0, 0)
    stack.append(current)
    visited.add(current)

    # DFS LOOP
    while stack:

        current = stack[-1]
        row, col = current

        neighbors = []

        if row > 0 and (row - 1, col) not in visited:
            neighbors.append((row - 1, col))
        if row < ROWS - 1 and (row + 1, col) not in visited:
            neighbors.append((row + 1, col))
        if col > 0 and (row, col - 1) not in visited:
            neighbors.append((row, col - 1))
        if col < COLS - 1 and (row, col + 1) not in visited:
            neighbors.append((row, col + 1))

        if neighbors:
            next_cell = random.choice(neighbors)
            r1, c1 = current
            r2, c2 = next_cell

            # remove wall
            if r2 == r1 + 1:
                northWall[r2][c2] = 0
            elif r2 == r1 - 1:
                northWall[r1][c1] = 0
            elif c2 == c1 + 1:
                eastWall[r1][c2] = 0
            elif c2 == c1 - 1:
                eastWall[r1][c1] = 0

            stack.append(next_cell)
            visited.add(next_cell)

        else:
            stack.pop()

    # ✅ THIS IS THE KEY PART (MUST BE HERE)
    start_col = random.randint(0, COLS - 1)
    end_col = random.randint(0, COLS - 1)

    northWall[0][start_col] = 0        # entrance (top)
    northWall[ROWS][end_col] = 0      # exit (bottom)