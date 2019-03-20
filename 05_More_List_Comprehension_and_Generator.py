#!/usr/bin/env python3.7

"""05_More_List_Comprehension_and_Generator.py.

Fifth Program of the Sentdex Intermediate Python Series.

"""

import logging
from platform import python_version
from sys import hexversion

PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_05.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("05_More_List_Comprehension_and_Generator.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]


input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]

'''
def div_by_five(num):
    """Docstring."""
    if num % 5 == 0:
        return True
    else:
        return False
'''


def div_by_five(num):
    """Docstring."""
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))
print("\n", "*" * 90)
for i in xyz:
    print("", i, end="+ ")
print("\n", "*" * 90)

xyz = (i for i in input_list if div_by_five(i))
print("\n", "*" * 90)
[print("", i, end="- ") for i in xyz]
print("\n", "*" * 90)

"""
you can not iterate over a generator twice.
a generator is exhausted once you have iterated over it.

"""

print("\n", "*" * 95)
[[print("", (i, ii), end=", ") for ii in range(3)] for i in range(3)]
print("\n", "*" * 95)

xyz = ([[i, ii] for ii in range(5)] for i in range(5))

print("\n", "*" * 95)
print([i for i in xyz])
print("\n", "*" * 95)

xyz = ([(i, ii) for ii in range(5)] for i in range(5))
print("\n", "*" * 95)
for i in xyz:
    print(i)
print("\n", "*" * 95)

xyz = (((i, ii) for ii in range(5)) for i in range(5))
print("\n", "*" * 95)
for i in xyz:
    for ii in i:
        print(ii)
print("\n", "*" * 95)

xyz = (print("", i, end=",") for i in range(5))
print("\n", "*" * 95)
for i in xyz:
    i
print("\n", "*" * 95)
