#!/usr/bin/python3
""" A model for the square new class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A constructor for the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """creating the init method"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """To be used as a function that will return info about
        the square class"""
        # self.__name__ is there to put the class name instead of rectangle
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of a given sqaure class parameters"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value    
