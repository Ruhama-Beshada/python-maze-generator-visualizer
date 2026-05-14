import random
from renderer import northWall, eastWall
from constants import *

class MazeSolver:
    def init(self):
        self.stack = []
        self.visited = set()

        self.current = (0, 0)
        self.stack.append(self.current)
        self.visited.add(self.current)

        self.solution_path = []
        self.dead_ends = []

    def can_move(self, a, b):
        r1, c1 = a
        r2, c2 = b

        # moving down
        if r2 == r1 + 1:
            return northWall[r2][c2] == 0

        # moving up
        if r2 == r1 - 1:
            return northWall[r1][c1] == 0

        # moving right
        if c2 == c1 + 1:
            return eastWall[r1][c2] == 0

        # moving left
        if c2 == c1 - 1:
            return eastWall[r1][c1] == 0

        return False

    def get_neighbors(self, cell):
        r, c = cell
        moves = []

        candidates = [
            (r-1, c),
            (r+1, c),
            (r, c-1),
            (r, c+1)
        ]

        for n in candidates:
            nr, nc = n

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if n not in self.visited and self.can_move(cell, n):
                    moves.append(n)

        return moves

    def step(self):
        if not self.stack:
            return False

        current = self.stack[-1]

        # EXIT CONDITION
        if current[0] == ROWS - 1:
            return False

        neighbors = self.get_neighbors(current)

        if neighbors:
            next_cell = random.choice(neighbors)

            self.stack.append(next_cell)
            self.visited.add(next_cell)
            self.solution_path.append(next_cell)

        else:
            self.dead_ends.append(self.stack.pop())

        return True