import pygame
from constants import *
from renderer import draw_maze
from maze_generator import MazeGenerator

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

clock = pygame.time.Clock()

generator = MazeGenerator()  # create generator

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # 👉 THIS IS THE MAGIC LINE (animation step)
    generator.step()

    draw_maze(screen)

    pygame.display.update()

pygame.quit()