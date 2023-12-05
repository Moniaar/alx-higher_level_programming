#!/usr/bin/python3
""" A module to print somthing special"""


def lookup(obj):
    """ A funtion that returns the list of available
    attributes and methods of an object

    Args:
        obj: a given object
    """
    return (dir(obj))
