#!/usr/bin/env python3.7

"""00_template.py.

Zeroeth Program of the Sentdex Intermediate Python Series.

"""

import logging
from platform import python_version
from sys import hexversion

VERSION_INFO = True
version_info = "The Python Version is: {}  #{}\n".format(
    python_version(), str((hexversion)))

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

[print(x, end="") for x in version_info if VERSION_INFO]

logging.basicConfig(filename="LOG_files/LOG_00.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info)
logger.info("00_template.py RUN / START")
