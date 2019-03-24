#!/usr/bin/env python3.7

"""18_Decorators.py.

Eighteenth Program of the Sentdex Intermediate Python Series.

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
logging.basicConfig(filename="LOG_files/LOG_18.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("18_Decorators.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

print("\nRussian Nesting Dolls")


def add_layer_description(style):
    """Description."""
    def add_layer(item):
        """Babushka Layer."""
        def layered_item():
            """combined."""
            return ('\n\t-a {} Babushka '
                    'concealing,{}'.format(style, str(item())))
        return layered_item
    return add_layer


@add_layer_description('lath turned')
@add_layer_description('carved')
@add_layer_description('painted')
@add_layer_description('wooden')
def chocolate():
    """Russian Nesting Dolls."""
    return '\n\t-a foil wrapped chocolate.'

print(chocolate())
'''
        $ ./18_Decorators.py
        Today is: Saturday, March, 23, 2019
        The Python Version is: 3.7.2  #50791152

        Russian Nesting Dolls

            -a lath turned Babushka concealing,
            -a carved Babushka concealing,
            -a painted Babushka concealing,
            -a wooden Babushka concealing,
            -a foil wrapped chocolate.
'''
