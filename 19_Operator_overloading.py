#!/usr/bin/env python3.5

"""19_Operator_overloading.py.

Nineteenth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion
import pygame
from datetime import datetime as dt
from element19 import Element
from random import randrange as rr

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_19.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("19_Operator_overloading.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


WIDTH = 1000
HEIGHT = 600

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

STARTING_BLUE_ELEMENTS = 10
STARTING_RED_ELEMENTS = 10
STARTING_GREEN_ELEMENTS = 10
STARTING_WHITE_ELEMENTS = 10


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("~ Element World ~")
clock = pygame.time.Clock()


class BlueElement(Element):
    """Docstring."""

    def __init__(self, x_bound, y_bound):
        """Docstring."""
        super().__init__((0, 0, 255), x_bound, y_bound)

    def move_unique(self):
        """Docstring."""
        self.x += rr(-10, 11)
        self.y += rr(-10, 11)


class GreenElement(Element):
    """Docstring."""

    def __init__(self, x_bound, y_bound):
        """Docstring."""
        super().__init__((0, 255, 0), x_bound, y_bound)

    def move_unique(self):
        """Docstring."""
        self.x += rr(-5, 6)
        self.y += rr(-5, 6)


class RedElement(Element):
    """Docstring."""

    def __init__(self, x_bound, y_bound):
        """Docstring."""
        super().__init__((255, 0, 0), x_bound, y_bound)

    def move_unique(self):
        """Docstring."""
        self.x += rr(-3, 4)
        self.y += rr(-3, 4)


class WhiteElement(Element):
    """Docstring."""

    def __init__(self, x_bound, y_bound):
        """Docstring."""
        super().__init__((255, 255, 255), x_bound, y_bound)

    def move_unique(self):
        """Docstring."""
        self.x += rr(-1, 2)
        self.y += rr(-1, 2)


def draw_environment(element_list):
    """Docstring."""
# Log v
    logger.info('-' * 45)
    logger.info(' {}\t{}\t {}\t{}'.format('#', '( x, y )', 'size', 'color'))
    logger.info('-' * 45)
# Log ^
    game_display.fill(BLACK)
    for colored_elements in element_list:
        for element_id in colored_elements:
            element = colored_elements[element_id]
# Log v
            logger.debug('{} \t{} \t\t{} \t{}'.format(
                element_id, (element.x, element.y),
                element.size, element.color))
# Log ^
            pygame.draw.circle(game_display, element.color,
                               [element.x, element.y], element.size)
            element.move_unique()
            element.check_bounds()

    pygame.display.update()


def main():
    """Docstring."""
    blue_elements = dict(
        enumerate([BlueElement(WIDTH, HEIGHT)for i in range(
            STARTING_BLUE_ELEMENTS)]))
    green_elements = dict(
        enumerate([GreenElement(WIDTH, HEIGHT)for i in range(
            STARTING_GREEN_ELEMENTS)]))
    red_elements = dict(
        enumerate([RedElement(WIDTH, HEIGHT)for i in range(
            STARTING_RED_ELEMENTS)]))
    white_elements = dict(
        enumerate([WhiteElement(WIDTH, HEIGHT)for i in range(
            STARTING_WHITE_ELEMENTS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([red_elements, blue_elements,
                          green_elements, white_elements])
        clock.tick(32)


if __name__ == '__main__':
    main()
