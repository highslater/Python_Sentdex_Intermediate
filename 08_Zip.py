#!/usr/bin/env python3.7

"""08_Zip.py.

Eighth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion

PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_08.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("08_Zip.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]


x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = list("abcd")

for a, b in zip(x, y):
    print(a, b, end=", ")
print()

for i in zip(x, y, z):
    print(i, end=", ")
print()

xx = [i for i in range(1, 11)]
yy = [i ** 2 for i in range(1, 11)]
xxyy = dict(zip(xx, yy))
print(xxyy)
