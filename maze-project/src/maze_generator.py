import random
from constants import *
from renderer import northWall, eastWall


class MazeGenerator:
    def __init__(self):
        self.stack = []
        self.visited = set()
        self.current = (0, 0)

        self.stack.append(self.current)
        self.visited.add(self.current)

    def get_neighbors(self, cell):
        row, col = cell
        neighbors = []

        if row > 0 and (row - 1, col) not in self.visited:
            neighbors.append((row - 1, col))

        if row < ROWS - 1 and (row + 1, col) not in self.visited:
            neighbors.append((row + 1, col))

        if col > 0 and (row, col - 1) not in self.visited:
            neighbors.append((row, col - 1))

        if col < COLS - 1 and (row, col + 1) not in self.visited:
            neighbors.append((row, col + 1))

        return neighbors

    def remove_wall(self, a, b):
        r1, c1 = a
        r2, c2 = b

        if r2 == r1 + 1:
            northWall[r2][c2] = 0
        elif r2 == r1 - 1:
            northWall[r1][c1] = 0
        elif c2 == c1 + 1:
            eastWall[r1][c2] = 0
        elif c2 == c1 - 1:
            eastWall[r1][c1] = 0

    # THIS IS THE IMPORTANT PART 👇
    def step(self):
        if not self.stack:
            return False  # DONE

        current = self.stack[-1]
        neighbors = self.get_neighbors(current)

        if neighbors:
            next_cell = random.choice(neighbors)

            self.remove_wall(current, next_cell)

            self.stack.append(next_cell)
            self.visited.add(next_cell)

        else:
            self.stack.pop()

        return True  # STILL RUNNING