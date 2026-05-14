import pygame
from constants import *
from renderer import draw_maze
from maze_generator import generate_maze
from maze_solver import MazeSolver

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

clock = pygame.time.Clock()

# GENERATE MAZE ONCE
generate_maze()

# CREATE SOLVER
solver = MazeSolver()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_maze(screen)

    solver.step()

    pygame.display.update()

pygame.quit()