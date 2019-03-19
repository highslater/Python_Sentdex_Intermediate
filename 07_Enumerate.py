#!/usr/bin/env python3.7

"""07_Enumerate.py.

Seventh Program of the Sentdex Intermediate Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_07.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("07_Enumerate.py RUN / START")
