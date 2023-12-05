#!/usr/bin/python3
""" a module to do somthing special """


def inherits_from(obj, a_class):
    """ a function to tell you which class is coming
    from which base one

    Args:
        obj: a given defalut object
        a_class: a base class to inhirit from
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
