#!/usr/bin/python3
"""making dictionaries"""


def class_to_json(obj):
    """a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object"""
    return obj.__dict__
