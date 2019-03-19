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


example = ['right', 'left', 'up', 'down']

for i in range(len(example)):
    print(i, example[i], end=", ")
print()

for i, j in enumerate(example):
    print(i, j, end=", ")
print()

new_dict = dict(enumerate(example))
print(new_dict)

x = [((k, v)) for k, v in new_dict.items()]
print(x)
