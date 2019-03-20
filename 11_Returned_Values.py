#!/usr/bin/env python3.7

"""11_Returned_Values.py.

Elevenenth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion
from multiprocessing import Pool


PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_11.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("11_Returned_Values.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]


def main():
    """Docstring."""
    data = []
    iterals = [range(10), range(20), [4], [4, 8], [4, 8, 12], [], range(21)]
    p = Pool(processes=20)

    for i in iterals:
        data.append(p.map(job, i))

    p.close()

    print_d(data)


def job(num):
    """Docstring."""
    return num * 2


def print_d(data):
    """Docstring."""
    [print(d) for d in data if d and len(d) < 21]


if __name__ == '__main__':
    main()
