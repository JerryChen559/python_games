import math
import random
import pygame
import tkinter as tk


class Cube(object):
    pass


class Snake(object):
    pass


def draw_grid(w, r, surface):
    size_between = w // r

    x = 0
    y = 0

    for line in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global rows, width

    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, items):
    pass


def main():
    global rows, width

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    # s = Snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)


# rows = 0
# w = 0
# h = 0

# Cube.rows = rows
# Cube.w = w

main()
