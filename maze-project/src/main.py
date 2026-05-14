import pygame
from constants import *
from renderer import draw_maze
from maze_generator import generate_maze
from maze_solver import MazeSolver

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

clock = pygame.time.Clock()

# STEP 1: generate maze ONCE
generate_maze()

# STEP 2: create solver
solver = MazeSolver()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    screen.fill(WHITE)

    # draw maze
    draw_maze(screen)

    # ⭐️ STEP 3: MOVE SOLVER ONE STEP PER FRAME
    solver.step()

    pygame.display.update()

pygame.quit()