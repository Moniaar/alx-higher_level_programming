#!/usr/bin/python3
"""A new module for the base class
that everyone is going to inhirit from"""


class Base:
    """Father class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the constrcutor for these upcoming classes too"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps.(list_dictionaries)
