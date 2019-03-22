#!/usr/bin/env python3.5

"""12_Spider_Example.py.

Twelfth Program of the Sentdex Intermediate Python Series.
had to bump down the python version to 3.5 to get all modules to work.

"""
import logging
import random  # noqa
import requests  # noqa
import string  # noqa
import bs4 as bs  # noqa
from platform import python_version
from sys import hexversion
from multiprocessing import Pool  # noqa


PRINT_VERSION_INFO = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str((hexversion)))
logging.basicConfig(filename="LOG_files/LOG_12.Log",
                    level=logging.ERROR, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("12_Spider_Example.py RUN / START")


def random_starting_url():
    """Docstring."""
    starting = ''.join(random.SystemRandom().choice(
        string.ascii_lowercase) for _ in range(3))
    return ''.join(['http://', starting, '.com'])


def handle_local_links(url, link):
    """Docstring."""
    return [''.join([url, link]), link][link.startswith('/')]


def get_links(url):
    """Docstring."""
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        # links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        logger.error("TypeError: {}.".format(str(e)))
        print("Got a TypeError")
        return []

    except IndexError as e:
        logger.error("IndexError: {}.".format(str(e)))
        print("Got a IndexError")
        return []

    except AttributeError as e:
        logger.error("AttributeError: {}.".format(str(e)))
        print("Got a AttributeError")
        return []

    except Exception as e:
        logger.error("Exception: {}.".format(str(e)))
        print("Got a General Exception, dunnno")
        return []

    else:
        pass
    finally:
        pass


def main():
    """Docstring."""
    how_many = 50
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('./Files/urls.txt', 'w') as f:
        for d in data:
            d = (d + ",\n")
            f.write(d)


if __name__ == '__main__':
    main()
