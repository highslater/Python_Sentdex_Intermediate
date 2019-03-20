#!/usr/bin/env python3.7

"""09_Wiriting_Generators.py.

Ninth Program of the Sentdex Intermediate Python Series.
"""
import logging
from platform import python_version
from sys import hexversion
import timeit

PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_09.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("09_Wiriting_Generators.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]

'''

def simple_gen():
    """Docstring."""
    yield("Oh")
    yield("Hello")
    yield("There")

for i in simple_gen():
    print(i, end=" ")

print()
'''

CORRECT_COMBO = (9, 9, 9)

'''

found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print("Found the combo: {}".format((c1, c2, c3)))
                found_combo = True
                break
            print((c1, c2, c3))
'''
g = ((c1, c2, c3)
     for c1 in range(10)
     for c2 in range(10)
     for c3 in range(10))

l = [(c1, c2, c3)
     for c1 in range(10)
     for c2 in range(10)
     for c3 in range(10)]


def combo_gen():
    """Docstring."""
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)


for (c1, c2, c3) in g:  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        print("Found the combo: {}".format((c1, c2, c3)))
        break
    # print((c1, c2, c3))


# ====== timeit ======

print("g = ", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)
g = ((c1, c2, c3)
    for c1 in range(10)
    for c2 in range(10)
    for c3 in range(10))

for (c1, c2, c3) in g:  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=50000))

print("l = ", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)
l = [(c1, c2, c3)
     for c1 in range(10)
     for c2 in range(10)
     for c3 in range(10)]

for (c1, c2, c3) in l:  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=50000))

print("combo_gen() = ", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)

for (c1, c2, c3) in combo_gen():  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=50000))


'''

$ ./09_Writing_a_Generator.py
The Python Version is: 3.7.2  #50791152
Found the combo: (9, 9, 9)
g =  17.42452411499835
l =  15.667225689001498
combo_gen() =  17.525755146001757
'''
