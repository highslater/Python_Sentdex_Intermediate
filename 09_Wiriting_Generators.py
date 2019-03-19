#!/usr/bin/env python3.7

"""09_Wiriting_Generators.py.

Ninth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion

PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

version_info = "The Python Version is: {}  #{}\n".format(
    python_version(), str((hexversion)))

[print(x, end="") for x in version_info if PRINT_VERSION_INFO]

logging.basicConfig(filename="LOG_files/LOG_09.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info)
logger.info("09_Wiriting_Generators.py RUN / START")
