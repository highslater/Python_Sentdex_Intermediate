#!/usr/bin/env python3.5

"""17SCRATCH_OOP_Introduction_5.py.

Seventeenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.

"""
import logging
import random
from platform import python_version
from sys import hexversion
import pygame
from datetime import datetime as dt
from element17 import Element

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_17S.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.debug("17SCRATCH_OOP_Introduction_5.py. RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

WIDTH = 1000
HEIGHT = 600

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

STARTING_BLUE_ELEMENTS = 1
STARTING_RED_ELEMENTS = 1
STARTING_GREEN_ELEMENTS = 1
STARTING_WHITE_ELEMENTS = 1

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("~ Element World ~")
clock = pygame.time.Clock()


def make_random_dict():
    """Docstring."""
    red_elements = list([Element(RED, WIDTH, HEIGHT)for i in range(
        STARTING_RED_ELEMENTS)])
    blue_elements = list([Element(BLUE, WIDTH, HEIGHT)for i in range(
        STARTING_BLUE_ELEMENTS)])
    green_elements = list([Element(GREEN, WIDTH, HEIGHT)for i in range(
        STARTING_GREEN_ELEMENTS)])
    white_elements = list([Element(WHITE, WIDTH, HEIGHT)for i in range(
        STARTING_WHITE_ELEMENTS)])

    el_list = red_elements + blue_elements + green_elements + white_elements
    random.shuffle(el_list)
    shuffled_dict = dict(enumerate(el_list))

    return shuffled_dict


def pygame_init(random_dict):
    """Docstring."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(random_dict)
        clock.tick(1)


def draw_environment(random_dict):
    """Docstring."""
    game_display.fill(BLACK)

    for element_id in random_dict:
        element = random_dict[element_id]
        pygame.draw.circle(game_display, element.color,
                           [element.x, element.y], element.size)
        element.move()
        element.check_bounds()

    pygame.display.update()


def main():
    """Docstring."""
    pygame_init(make_random_dict())


if __name__ == '__main__':
    main()
