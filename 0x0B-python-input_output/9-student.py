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
