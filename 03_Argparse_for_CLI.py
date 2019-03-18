#!/usr/bin/env python3.7

"""03_Argparse_for_CLI.py.

Third Program of the Sentdex Intermediate Python Series.

"""
import logging
import argparse
import sys


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_03.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("03_Argparse_for_CLI.py RUN / START")


def main():
    """Docstring."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul, div)')

    args = parser.parse_args()
    sys.stdout.write("\t")
    sys.stdout.write("Answer: " + str(calc(args)) + "\n")
    # print("\tAnswer: " + str(calc(args)) + "\n")

'''

$ ./03_Argparse_for_CLI.py -h
usage: 03_Argparse_for_CLI.py [-h] [--x X] [--y Y] [--operation OPERATION]

optional arguments:
  -h, --help            show this help message and exit
  --x X                 What is the first number?
  --y Y                 What is the second number?
  --operation OPERATION
                        What operation? (add, sub, mul, div)

$ ./03_Argparse_for_CLI.py --x=5 --y=2 --operation=mul
10.0


'''


def calc(args):
    """Docstring."""
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()
