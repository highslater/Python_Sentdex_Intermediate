#!/usr/bin/env python3.5

"""element17.py.

MODULE for Seventeenth Program of the Sentdex Intermediate Python Series.
downgraded to accomodate pygame module.
"""

from random import randrange as rr


class Element():
    """docstring for Element."""

    def __init__(self, color, x_bound,
                 y_bound, size_range=(5, 10), movement_range=(-1, 2)):
        """Docstring."""
        self.color = color
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.x = rr(0, self.x_bound)
        self.y = rr(0, self.y_bound)
        self.size = rr(size_range[0], size_range[1])
        self.movement_range = movement_range

    def move(self):
        """Docstring."""
        self.move_x = rr(self.movement_range[0], self.movement_range[1])
        self.move_y = rr(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        """Docstring."""
        self.x = 0 if self.x < 0 else (
            self.x_bound if self.x > self.x_bound else self.x)
        self.y = 0 if self.y < 0 else (
            self.y_bound if self.y > self.y_bound else self.y)


class BlueElement(Element):
    """Docstring."""

    def __init__(self, color, x_bound, y_bound):
        """Docstring."""
        super().__init__(color, x_bound, y_bound)
        self.color = color

    def move_unique(self):
        """Docstring."""
        self.x += rr(-12, 13)
        self.y += rr(-12, 13)


class GreenElement(Element):
    """Docstring."""

    def __init__(self, color, x_bound, y_bound):
        """Docstring."""
        super().__init__(color, x_bound, y_bound)
        self.color = color

    def move_unique(self):
        """Docstring."""
        self.x += rr(-6, 7)
        self.y += rr(-6, 7)


class RedElement(Element):
    """Docstring."""

    def __init__(self, color, x_bound, y_bound):
        """Docstring."""
        super().__init__(color, x_bound, y_bound)
        self.color = color

    def move_unique(self):
        """Docstring."""
        self.x += rr(-4, 5)
        self.y += rr(-4, 5)


class WhiteElement(Element):
    """Docstring."""

    def __init__(self, color, x_bound, y_bound):
        """Docstring."""
        super().__init__(color, x_bound, y_bound)
        self.color = color

    def move_unique(self):
        """Docstring."""
        self.x += rr(-2, 3)
        self.y += rr(-2, 3)
