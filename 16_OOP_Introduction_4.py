#!/usr/bin/env python3.5

"""16_OOP_Introduction_4.py.py.

Sixteenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.

"""
import logging
from platform import python_version
from sys import hexversion
import pygame  # noqa
import random
from datetime import datetime as dt


NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_16.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.debug("16_OOP_Introduction_4.py. RUN / START")

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


class Element():
    """docstring for Element."""

    def __init__(self, color):
        """Docstring."""
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.color = color
        self.size = random.randrange(5, 10)

    def move(self):
        """Docstring."""
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT


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
            element.move()
    pygame.display.update()


def main():
    """Docstring."""
    red_elements = dict(
        enumerate(
            [Element(color=RED)for i in range(STARTING_RED_ELEMENTS)]))
    blue_elements = dict(
        enumerate([
            Element(color=BLUE)for i in range(STARTING_BLUE_ELEMENTS)]))
    green_elements = dict(
        enumerate(
            [Element(color=GREEN)for i in range(STARTING_GREEN_ELEMENTS)]))
    white_elements = dict(
        enumerate(
            [Element(color=WHITE)for i in range(STARTING_WHITE_ELEMENTS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([red_elements, blue_elements,
                          green_elements, white_elements])
        clock.tick(1)


if __name__ == '__main__':
    main()
