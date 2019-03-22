#!/usr/bin/env python3.5

"""15_OOP_Introduction_3.py.py.

Fifteenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.

"""
import logging
from platform import python_version
from sys import hexversion
import pygame  # noqa
import random


PRINT_VERSION_INFO = False
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_15.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("15_OOP_Introduction_3.py RUN / START")


WIDTH = 800
HEIGHT = 600

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

STARTING_BLUE_ELEMENTS = 10
STARTING_RED_ELEMENTS = 3


# pygame.init()
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
        self.size = random.randrange(50, 70)

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

        # self.x = [0, self.x][self.x < 0]
        # self.x = [WIDTH, self.x][self.x > WIDTH]

        # self.x = [[0, self.x][WIDTH, self.x]][[self.x < 0][self.x > WIDTH]]

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT

        # self.y = [0, self.y][self.y < 0]
        # self.y = [HEIGHT, self.y][self.y > HEIGHT]

        # self.y = [[0, self.y][HEIGHT, self.y]][[self.y < 0][self.y > HEIGHT]]


def draw_environment(element):
    """Docstring."""
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, element.color,
                       [element.x, element.y], element.size)
    pygame.display.update()
    element.move()


def main():
    """Docstring."""
    red_element = Element(color=RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(red_element)
        clock.tick(60)


if __name__ == '__main__':
    main()
