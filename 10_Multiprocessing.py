#!/usr/bin/env python3.7

"""10_Multiprocessing.py.

Tenth Program of the Sentdex Intermediate Python Series.

"""
import logging
from platform import python_version
from sys import hexversion

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
