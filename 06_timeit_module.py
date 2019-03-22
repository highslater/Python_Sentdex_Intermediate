#!/usr/bin/env python3.7

"""06_timeit_module.py.

Sixth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion
import timeit

PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_06.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("06_timeit_module.py RUN / START")


print("GENERATE= ", timeit.timeit("""
input_list = range(100)


def div_by_five1(num):
    '''Docstring.'''
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five1(i))""", number=500000))

print("LIST = ", timeit.timeit("""
input_list = range(100)


def div_by_five2(num):
    '''Docstring.'''
    return num % 5 == 0

xyz = [i for i in input_list if div_by_five2(i)]""", number=500000))

print("GENERATE / ITERATE = ", timeit.timeit("""
input_list = range(100)


def div_by_five1(num):
    '''Docstring.'''
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five1(i))
for i in xyz:
    x = i""", number=500000))

print("LIST / ITERATE = ", timeit.timeit("""
input_list = range(100)


def div_by_five2(num):
    '''Docstring.'''
    return num % 5 == 0

xyz = [i for i in input_list if div_by_five2(i)]
for i in xyz:
    x = i""", number=500000))


'''

$ ./06_timeit_module.py

        GENERATE=  0.6251755740013323
        LIST =  12.204710392994457
        GENERATE / ITERATE =  12.580771048997121
        LIST / ITERATE =  12.719103055002051

'''
