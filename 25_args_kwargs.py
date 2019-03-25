#!/usr/bin/env python3.5

"""25_args_kwargs.py.

Twenty-Fifth Program of the Sentdex Intermediate Python Series.

"""
import logging
import matplotlib.pyplot as plt
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_25.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("25_args_kwargs.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

# Args and Kwargs

blog_1 = "I am so awesome."
blog_2 = "Cars are cool."
blog_3 = "Aw look at my cat."

site_title = 'My Blog'


def blog_posts1(title, *args):
    """Docstring."""
    print("", title)
    for post in args:
        print("", post)


def blog_posts2(title, **kwargs):
    """Docstring."""
    print("", title)
    for p_title, post in kwargs.items():
        print("", p_title, post)


def blog_posts3(title, *args, **kwargs):
    """Docstring."""
    print("", title)
    for arg in args:
        print('', arg)
    for p_title, post in kwargs.items():
        print("", p_title, post)


print('', "*" * 88)
blog_posts1(site_title, blog_1, blog_2, blog_3)
print('\n', "*" * 88)

print('', "*" * 88)
blog_posts2(site_title, blog_1="I am so awesome.",
            blog_2="Cars are cool.",
            blog_3="Aw look at my cat.")
print('\n', "*" * 88)

print('', "*" * 88)
blog_posts3(site_title,
            '1', '2', '3',
            blog_1="I am so awesome.",
            blog_2="Cars are cool.",
            blog_3="Aw look at my cat.")
print('\n', "*" * 88)


def graph_operation(x, y):
    """Docstring."""
    print('function that graphs {} and {}'.format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [2, 3, 4, 5, 6, 1, 2]
y1 = [1, 2, 0, 2, 0, 2, 1]

graph_me = [x1, y1]

# print('', "*" * 88)
# graph_operation(x1, y1)
# print('\n', "*" * 88)

print('', "*" * 88)
graph_operation(*graph_me)
print('\n', "*" * 88)
