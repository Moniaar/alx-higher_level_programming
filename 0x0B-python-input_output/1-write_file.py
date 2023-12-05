#!/usr/bin/python3
"""This is a remarkable module """


def write_file(filename="", text=""):
    """A function to write into a file from a user """
    with open(filename, ,'w', encoding='utf-8') as f:
        return f.write(text)
