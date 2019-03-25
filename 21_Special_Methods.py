#!/usr/bin/env python3.7

"""21_a_Special_Methods.py.

Twenty-First (a) Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_21_a.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("21_a_Special_Methods.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

x = (i for i in range(10))

print("", "*" * 90)
[print(i, end=", ") for i in x]
print("\n", "*" * 90)

x = (i for i in range(10))
next(x)
next(x)
next(x)
print("", "*" * 90)
[print(i, end=", ") for i in x]
print("\n", "*" * 90)

x = (i for i in range(10))
x.__next__()
x.__next__()
x.__next__()
print("", "*" * 90)
[print(i, end=", ") for i in x]
print("\n", "*" * 90)

x = (i for i in range(10))

print("", "*" * 90)
print(dir(x))
print("\n", "*" * 90)

'''
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__',
 '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
'''

print("", "*" * 90)
# print(help(x.__next__))
print("\n", "*" * 90)


class RangeExample():
    """docstring for RangeExample."""

    def __init__(self, end, step=1):
        """Docstring."""
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        """Docstring."""
        return self

    def __next__(self):
        """Docstring."""
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_value = self.current
            self.current += self.step
            return return_value

print("", "*" * 90)
for i in RangeExample(15):
    print(i, end=", ")
print("\n", "*" * 90)

x = (i for i in RangeExample(15))
x.__next__()
x.__next__()
x.__next__()
next(x)
next(x)
next(x)
print("", "*" * 90)
[print(i, end=", ") for i in x]
print("\n", "*" * 90)

x = (i for i in RangeExample(15))


def range_gen(end):
    """Docstring."""
    current = 0
    while current < end:
        yield current
        current += 1

print("", "*" * 90)
for i in range_gen(5):
    print(i, end=", ")
print("\n", "*" * 90)

x = range_gen(5)
x.__next__()

print("", "*" * 90)
for i in x:
    print(i, end=", ")
print("\n", "*" * 90)
