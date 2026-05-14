import random
from renderer import northWall, eastWall, solver_path, dead_ends
from constants import *


class MazeSolver:

    def __init__(self):

        self.stack = []
        self.visited = set()

        # START TOP-LEFT
        self.current = (0, 0)

        self.stack.append(self.current)
        self.visited.add(self.current)

    def can_move(self, a, b):

        r1, c1 = a
        r2, c2 = b

        if r2 == r1 + 1:
            return northWall[r2][c2] == 0

        if r2 == r1 - 1:
            return northWall[r1][c1] == 0

        if c2 == c1 + 1:
            return eastWall[r1][c2] == 0

        if c2 == c1 - 1:
            return eastWall[r1][c1] == 0

        return False

    def get_neighbors(self, cell):

        r, c = cell

        moves = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        result = []

        for nr, nc in moves:
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if (nr, nc) not in self.visited:
                    if self.can_move(cell, (nr, nc)):
                        result.append((nr, nc))

        return result

    def step(self):

        if not self.stack:
            return False

        current = self.stack[-1]

        # END = BOTTOM-RIGHT
        if current == (ROWS - 1, COLS - 1):
            return False

        neighbors = self.get_neighbors(current)

        if neighbors:
            nxt = random.choice(neighbors)

            self.stack.append(nxt)
            self.visited.add(nxt)

            solver_path.append(nxt)

        else:
            dead_ends.append(self.stack.pop())

        return True