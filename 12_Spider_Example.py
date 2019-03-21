#!/usr/bin/env python3.5

"""12_Spider_Example.py.

Twelfth Program of the Sentdex Intermediate Python Series.

"""
import logging
import random  # noqa
import requests  # noqa
import string  # noqa
import bs4 as bs  # noqa
from platform import python_version
from sys import hexversion
from multiprocessing import Pool  # noqa


PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_12.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
[logger.debug(version_info), None][PRINT_VERSION_INFO]
logger.info("12_Spider_Example.py RUN / START")

[print(version_info), None][PRINT_VERSION_INFO]


def random_starting_url():
    """Docstring."""
    starting = ''.join(random.SystemRandom().choice(
        string.ascii_lowercase) for _ in range(3))
    return ''.join(['http://', starting, '.com'])

# url = random_starting_url()
# print(url)


def handle_local_links(url, link):
    """Docstring."""
    return [''.join([url, link]), link][link.startswith('/')]
