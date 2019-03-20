#!/usr/bin/env python3.7

"""10_Multiprocessing.py.

Tenth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion
import multiprocessing


PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_10.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("10_Multiprocessing.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]


def spawn(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    """Docstring."""
    print('Spawned!{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(num1, num2,
                                                              num3, num4,
                                                              num5, num6,
                                                              num7, num8,
                                                              num9, num10))

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(
            target=spawn,
            args=(i, i ** 2, i ** 3, i ** 4, i ** 5,
                  i ** 6, i ** 7, i ** 8, i ** 9, i ** 10)
        p.start()
        p.join()
