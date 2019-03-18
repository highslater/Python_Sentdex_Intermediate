#!/usr/bin/env python3.7

"""00_template.py.

Zeroeth Program of the Sentdex Intermediate Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_00.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("00_template.py RUN / START")
