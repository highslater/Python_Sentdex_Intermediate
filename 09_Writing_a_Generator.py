#!/usr/bin/env python3.7

"""09_Wiriting_Generators.py.

Ninth Program of the Sentdex Intermediate Python Series.
"""
import logging
from platform import python_version
from sys import hexversion
import timeit
import time

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

print("g = \t\t", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)
g = ((c1, c2, c3)
    for c1 in range(10)
    for c2 in range(10)
    for c3 in range(10))

for (c1, c2, c3) in g:  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=10000))

print("l = \t\t", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)
l = [(c1, c2, c3)
     for c1 in range(10)
     for c2 in range(10)
     for c3 in range(10)]

for (c1, c2, c3) in l:  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=10000))

print("combo_gen() = \t", timeit.timeit("""
CORRECT_COMBO = (9, 9, 9)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)

for (c1, c2, c3) in combo_gen():  # combo_gen() or g or l
    if (c1, c2, c3) == CORRECT_COMBO:
        break
""", number=10000))


gi = time.time()

for i in range(10000):
    g = ((c1, c2, c3)
         for c1 in range(10)
         for c2 in range(10)
         for c3 in range(10))

    for (c1, c2, c3) in g:
        if (c1, c2, c3) == CORRECT_COMBO:
            break

gf = time.time()
print("g Elapsed Time: ", (gf - gi))


li = time.time()

for i in range(10000):
    for (c1, c2, c3) in l:
        if (c1, c2, c3) == CORRECT_COMBO:
            break

lf = time.time()
print("l Elapsed Time: ", (lf - li))


ci = time.time()

for i in range(10000):
    for (c1, c2, c3) in combo_gen():
        if (c1, c2, c3) == CORRECT_COMBO:
            break

cf = time.time()
print("c Elapsed Time: ", (cf - ci))

"""
$ ./09_Writing_a_Generator.py
The Python Version is: 3.7.2  #50791152
Found the combo: (9, 9, 9)
g =              3.5394026229987503
l =              3.162731858996267
combo_gen() =    3.5409054440024192

g Elapsed Time:  5.799894094467163
l Elapsed Time:  3.729189395904541
c Elapsed Time:  5.822967290878296

"""
