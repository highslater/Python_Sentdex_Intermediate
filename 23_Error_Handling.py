#!/usr/bin/env python3.5

"""23_Error_Handling.py.

Twenty-Second Program of the Sentdex Intermediate Python Series.

"""
import logging
import sys
from platform import python_version
from sys import hexversion
from datetime import datetime as dt


NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_23.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("23_Error_Handling.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


def error_handler():
    """Docstring."""
    return 'Line:{}, {}, {}'.format(sys.exc_info()[2].tb_lineno,
                                    sys.exc_info()[0],
                                    sys.exc_info()[1])
try:
    a + b
except Exception as e:
    logging.error(error_handler())
    print(sys.exc_info())
else:
    pass
finally:
    pass
