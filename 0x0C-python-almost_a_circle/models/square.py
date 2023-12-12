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
        return '[{}] ({}) {}/{} - {}'. format(
                type(self).__name__, self.id, self.x,
                self.y, self.width)

    @property
    def size(self):
        """size of a given sqaure class parameters"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """assigns a key/value argument to attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """assigns an arguments to each attributes of the class"""
        # do task 8 question, skip kwargs is args are passed
        if args:
            self.__update(*args)
        # ** means break the dictionary value into keys and values
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Method that returns the dictionary
        representation of a Rectangle"""
        # this will work for task 14 only
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
