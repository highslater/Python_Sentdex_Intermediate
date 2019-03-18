#!/usr/bin/env python3.7

"""04_List_Comprehension_and_Generator.py.

ZFourth Program of the Sentdex Intermediate Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_04.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("04_List_Comprehension_and_Generator.py RUN / START")
