#!/usr/bin/python3
""" a module to do somethins special"""


def is_kind_of_class(obj, a_class):
    """ a function that returns True if the object is
    exactly an instance of the specified class ; otherwise False

    Args:
        obj: given object
        a_class: parent class
    """
    return isinstance(obj, a_class)
