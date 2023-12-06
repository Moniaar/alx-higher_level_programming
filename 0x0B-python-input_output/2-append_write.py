#!/usr/bin/python3
"""This is a remarkable module """


def append_file(filename="", text=""):
    """A function to append into a file from a user """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
