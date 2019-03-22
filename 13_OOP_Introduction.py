#!/usr/bin/env python3.5

"""13_OOP_Introduction.py.

Thirteenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.

"""
import logging
from platform import python_version
from sys import hexversion
import pygame  # noqa
import random


PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_13.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("13_OOP_Introduction.py RUN / START")


WIDTH = 0
HEIGHT = 0


class Element():
    """docstring for Element."""

    def __init__(self, color, name, symbol, number,
                 atomic_weight, atomic_number):
        """Docstring."""
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.color = color
        self.name = name
        self.symbol = symbol
        self.number = number
        self.atomic_weight = atomic_weight
        self.atomic_number = atomic_number

    def move(self):
        """Docstring."""
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        # if self.x < 0:
        #     self.x = 0
        # elif self.x > WIDTH:
        #     self.x = WIDTH

        # self.x = [0, self.x][self.x < 0]
        # self.x = [WIDTH, self.x][self.x > WIDTH]

        self.x = [[0, self.x][WIDTH, self.x]][[self.x < 0][self.x > WIDTH]]

        # if self.y < 0:
        #     self.y = 0
        # elif self.y > HEIGHT:
        #     self.y = HEIGHT

        # self.y = [0, self.y][self.y < 0]
        # self.y = [HEIGHT, self.y][self.y > HEIGHT]

        self.y = [[0, self.y][HEIGHT, self.y]][[self.y < 0][self.y > HEIGHT]]
