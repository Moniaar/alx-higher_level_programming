#!/usr/bin/python3
"""classed with json module """


class Student:
    """a class to save student data"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a function that retrieves a dictionary
        representation of a Student instance"""
        return self.__dict__
    try:
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
    except Exception:
        return self.__dict__
    my_dict = dict()
    for key, value in self.__dict__.items():
        if key in attrs:
            my_dict[key] = value
    return my_dict
