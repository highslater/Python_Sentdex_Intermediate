#!/usr/bin/env python3.5

"""element17.py.

MODULE for Seventeenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.

"""

import random


class Element():
    """docstring for Element."""

    def __init__(self, x_bound, y_bound, color,
                 size_range=(5, 10), movement_range=(-1, 2)):
        """Docstring."""
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.color = color
        self.size = random.randrange(size_range[0], size_range[1])
        self.x = random.randrange(0, self.x_bound)
        self.y = random.randrange(0, self.y_bound)
        self.movement_range = movement_range

    def move(self):
        """Docstring."""
        self.move_x = random.randrange(
            self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(
            self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        """Docstring."""
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_bound:
            self.x = self.x_bound

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_bound:
            self.y = self.y_bound
