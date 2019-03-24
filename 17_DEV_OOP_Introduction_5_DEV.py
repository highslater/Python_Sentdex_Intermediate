#!/usr/bin/env python3.5

"""17_DEV_OOP_Introduction_5_DEV.py.

Seventeenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.
"""
from random import shuffle
import pygame
from element17_DEV import Element as El  # noqa
from element17_DEV import BlueElement as BEl
from element17_DEV import GreenElement as GEl
from element17_DEV import RedElement as REl
from element17_DEV import WhiteElement as WEl

W, H = 1000, 600
BLACK, BLUE = (0, 0, 0), (0, 0, 255)
GREEN, RED, WHITE = (0, 255, 0), (255, 0, 0), (255, 255, 255)
NUM_BLUE, NUM_RED, NUM_GREEN, NUM_WHITE = 5, 5, 5, 5

game_display = pygame.display.set_mode((W, H))
pygame.display.set_caption("DEV ~ Element World ~ DEV")
clock = pygame.time.Clock()


def params():
    """Docstring."""
    elist = [
        *[REl(RED, W, H)for i in range(NUM_RED)],
        *[BEl(BLUE, W, H)for i in range(NUM_BLUE)],
        *[GEl(GREEN, W, H)for i in range(NUM_GREEN)],
        *[WEl(WHITE, W, H)for i in range(NUM_WHITE)]]
    shuffle(elist)
    return dict(enumerate(elist))


def pygame_init(random_dict):
    """Docstring."""
    while True:
        [(pygame.quit(), quit())
            for event in pygame.event.get() if event.type == pygame.QUIT]
        draw_environment(random_dict)
        clock.tick(32)


def draw_environment(random_dict):
    """Docstring."""
    game_display.fill(BLACK)
    [(pygame.draw.circle(game_display, el.color, [el.x, el.y], el.size),
      el.move_unique(),
      el.check_bounds()) for k, el in random_dict.items()]
    pygame.display.update()


if __name__ == '__main__':
    pygame_init(params())
