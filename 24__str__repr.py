#!/usr/bin/env python3.5

"""24__str__repr.py.

Twenty-fourth  Program of the Sentdex Intermediate Python Series.

"""
import logging
import pygame
import numpy as np
from platform import python_version
from sys import hexversion
from datetime import datetime as dt
from element24 import Element
from random import randrange as rr


NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_24.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("24__str__repr.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

WIDTH = 1000
HEIGHT = 600

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

STARTING_BLUE_ELEMENTS = 5
STARTING_RED_ELEMENTS = 15
STARTING_GREEN_ELEMENTS = 15
STARTING_WHITE_ELEMENTS = 15

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("~ Element World ~")
clock = pygame.time.Clock()


class BlueElement(Element):
    """Docstring."""

    def __init__(self, x_bound, y_bound):
        """Docstring."""
        super().__init__((0, 0, 255), x_bound, y_bound)

    def __add__(self, other_element):
        """Operator Overload ( + )."""
# Log v
        if self.color != other_element.color:
            logging.info("+ OP --> {}\t +\t {}".format(
                repr(self), repr(other_element)))
# Log ^
        if other_element.color == (255, 0, 0):
            self.size -= other_element.size
            other_element.size -= self.size

        elif other_element.color == (0, 255, 0):
            self.size += other_element.size
            other_element.size = 0

        elif other_element.color == (255, 255, 255):
            self.size += other_element.size
            other_element.size = 0

        elif other_element.color == (0, 0, 255):
            pass

        else:
            raise Exception('Nope UNSUPPORTED color')

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


def is_touching(e1, e2):
    """Docstring."""
    return (np.linalg.norm(
        np.array([e1.x, e1.y]) - np.array([e2.x, e2.y])) < (e1.size + e2.size))


def collision_handler(element_list):
    """Docstring."""
    blues, greens, reds, whites = element_list
    for blue_id, blue_element in blues.copy().items():
        for other_elements in blues, greens, reds, whites:
            for other_element_id, other_element in (
                    other_elements.copy().items()):
                if blue_element == other_element:
                    pass
                else:
                    if is_touching(blue_element, other_element):
                        blue_element + other_element
                        if other_element.size <= 0:
                            del other_elements[other_element_id]
                        if blue_element.size <= 0:
                            del blues[blue_id]

    return blues, greens, reds, whites


def draw_environment(element_list):
    """Docstring."""
# Log v
    # logger.info('-' * 45)
    # logger.info(' {}\t{}\t {}\t{}'.format('#', '( x, y )', 'size', 'color'))
    # logger.info('-' * 45)
# Log ^
    blues, greens, reds, whites = collision_handler(element_list)
    game_display.fill(BLACK)
    for colored_elements in element_list:
        for element_id in colored_elements:
            element = colored_elements[element_id]
# Log v
            # logger.debug('{} \t{} \t\t{} \t{}'.format(
            #     element_id, (element.x, element.y),
            #     element.size, element.color))
# Log ^
            pygame.draw.circle(game_display, element.color,
                               [element.x, element.y], element.size)

            if element.color == (0, 0, 255):
                element.move_unique()
            else:
                element.move()
            element.check_bounds()

    pygame.display.update()
    return blues, greens, reds, whites


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

# Log v
    # logger.info("")

    # logger.info("~ Blue + Red collision ~")
    # logger.info(('BlueElement size = {}, RedElement size = {}'.format(
    #     blue_elements[0].size, red_elements[0].size)))
    # blue_elements[0] + red_elements[0]
    # logger.info(('BlueElement size = {}, RedElement size = {}'.format(
    #     blue_elements[0].size, red_elements[0].size)))
    # logger.info("~ Blue + Red collision ~")

    # logger.info("")

    # logger.info("~ Blue + Green collision ~")
    # logger.info(('BlueElement size = {}, GreenElement size = {}'.format(
    #     blue_elements[1].size, green_elements[1].size)))
    # blue_elements[1] + green_elements[1]
    # logger.info(('BlueElement size = {}, GreenElement size = {}'.format(
    #     blue_elements[1].size, green_elements[1].size)))
    # logger.info("~ Blue + Green collision ~")

    # logger.info("")

    # logger.info("~ Blue + White collision ~")
    # logger.info(('BlueElement size = {}, WhiteElement size = {}'.format(
    #     blue_elements[2].size, white_elements[2].size)))
    # blue_elements[2] + white_elements[2]
    # logger.info(('BlueElement size = {}, WhiteElement size = {}'.format(
    #     blue_elements[2].size, white_elements[2].size)))
    # logger.info("~ Blue + White collision ~")

    # logger.info("")

    # logger.info("~ Blue + Blue collision ~")
    # logger.info(('BlueElement size = {}, BlueElement size = {}'.format(
    #     blue_elements[3].size, blue_elements[4].size)))
    # blue_elements[3] + blue_elements[4]
    # logger.info(('BlueElement size = {}, BlueElement size = {}'.format(
    #     blue_elements[3].size, blue_elements[4].size)))
    # logger.info("~ Blue + Blue collision ~")
# Log ^

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blue_elements, green_elements, red_elements, white_elements = (
            draw_environment([blue_elements,
                             green_elements, red_elements, white_elements]))
        clock.tick(32)


if __name__ == '__main__':
    # exec(open("24__str__repr.py").read()
    main()
