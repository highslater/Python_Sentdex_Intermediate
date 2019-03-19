#!/usr/bin/env python3.7

"""04_List_Comprehension_and_Generator.py.

Fourth Program of the Sentdex Intermediate Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_04.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("04_List_Comprehension_and_Generator.py RUN / START")

list_1 = [i for i in range(5)]

list_2 = []
for i in range(5):
    list_2.append(i)

print("*" * 90)
print(list_1 == list_2)
print("*" * 90)

g_1 = (i for i in range(10))

print("*" * 90)
for i in g_1:
    print(i, end=", ")

print("11111")
g_1 = (i for i in range(10))
[print(i) for i in g_1]
print("11111")

print()
print("*" * 90)


def gen():
    """Docstring."""
    for x in range(10):
        yield x

g_2 = gen()

print("*" * 90)
for i in g_2:
    print(i, end=", ")

print("22222")
[print(i) for i in gen()]
print("22222")

print()
print("*" * 90)

print("*" * 90)
print(g_1)
print(g_2)
print(g_1 == g_2)
print("*" * 90)

print("*" * 90)
print(list_1)
print(g_1)
print("*" * 90)
