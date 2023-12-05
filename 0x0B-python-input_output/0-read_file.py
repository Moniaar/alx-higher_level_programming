#!/usr/bin/python3
"""This is a remarkable module """


def read_file(filename=""):
    """A function to read the file from a user """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
