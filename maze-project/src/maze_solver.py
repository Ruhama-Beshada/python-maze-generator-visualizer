import random
from renderer import northWall, eastWall, solver_path, dead_ends
from constants import *

class MazeSolver:
    def __init__(self):
        """
        Initializes the solver with a stack for DFS and a visited set 
        to track explored cells.
        """
        self.stack = []
        self.visited = set()

        # Start at the entrance (top-left)
        self.current = (0, 0)
        self.stack.append(self.current)
        self.visited.add(self.current)
        
        # Initialize the visual path with the starting point
        solver_path.clear()
        solver_path.append(self.current)

    def can_move(self, a, b):
        """
        Checks if there is a path between cell 'a' and cell 'b' 
        by verifying the wall arrays.
        """
        r1, c1 = a
        r2, c2 = b

        # move down
        if r2 == r1 + 1:
            return northWall[r2][c2] == 0

        # move up
        if r2 == r1 - 1:
            return northWall[r1][c1] == 0

        # move right
        if c2 == c1 + 1:
            return eastWall[r1][c2] == 0

        # move left
        if c2 == c1 - 1:
            return eastWall[r1][c1] == 0

        return False

    def get_neighbors(self, cell):
        """
        Returns a list of unvisited neighbors that are accessible (no walls).
        """
        r, c = cell
        moves = []

        candidates = [
            (r - 1, c), # Up
            (r + 1, c), # Down
            (r, c - 1), # Left
            (r, c + 1)  # Right
        ]

        for n in candidates:
            nr, nc = n

            # Check boundaries
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                # Check if unvisited AND no wall exists
                if n not in self.visited and self.can_move(cell, n):
                    moves.append(n)

        return moves

    def step(self):
        """
        Executes one step of the DFS algorithm.
        Updates the global solver_path to reflect the current active search.
        """
        if not self.stack:
            return False

        current = self.stack[-1]

        # EXIT CONDITION: Reached the bottom row
        if current[0] == ROWS - 1:
            return False

        neighbors = self.get_neighbors(current)

        if neighbors:
            # Choose a random valid neighbor and move forward
            next_cell = random.choice(neighbors)

            self.stack.append(next_cell)
            self.visited.add(next_cell)

            # Update visual path to match the stack (Correct path)
            solver_path.clear()
            solver_path.extend(self.stack)

        else:
            # No neighbors? Backtrack.
            backtracked_cell = self.stack.pop()
            dead_ends.append(backtracked_cell)

            # Update visual path to remove the dead-end from the "red dots"
            solver_path.clear()
            solver_path.extend(self.stack)

        return True