import pygame
from constants import *

# =========================
# MAZE WALL DATA
# =========================
northWall = [[1 for _ in range(COLS)] for _ in range(ROWS + 1)]
eastWall = [[1 for _ in range(COLS + 1)] for _ in range(ROWS)]

# =========================
# SOLVER VISUAL DATA
# =========================
solver_path = []
dead_ends = []


def draw_maze(screen):

    start_x = 50
    start_y = 50

    # =========================
    # DRAW NORTH WALLS
    # =========================
    for row in range(ROWS + 1):
        for col in range(COLS):

            if northWall[row][col] == 1:

                x1 = start_x + col * CELL_SIZE
                y1 = start_y + row * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1

                pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)

    # =========================
    # DRAW EAST WALLS
    # =========================
    for row in range(ROWS):
        for col in range(COLS + 1):

            if eastWall[row][col] == 1:

                x1 = start_x + col * CELL_SIZE
                y1 = start_y + row * CELL_SIZE

                x2 = x1
                y2 = y1 + CELL_SIZE

                pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)

    # =========================
    # DRAW SOLVER PATH (RED)
    # =========================
    for r, c in solver_path:

        cx = start_x + c * CELL_SIZE + CELL_SIZE // 2
        cy = start_y + r * CELL_SIZE + CELL_SIZE // 2

        pygame.draw.circle(screen, (255, 0, 0), (cx, cy), 5)

    # =========================
    # DRAW DEAD ENDS (BLUE)
    # =========================
    for r, c in dead_ends:

        cx = start_x + c * CELL_SIZE + CELL_SIZE // 2
        cy = start_y + r * CELL_SIZE + CELL_SIZE // 2

        pygame.draw.circle(screen, (0, 0, 255), (cx, cy), 5)