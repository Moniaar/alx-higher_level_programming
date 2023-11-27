#!/usr/bin/python3
"""creating a module to handle a Rectangle object"""


class Rectangle:
    """Defining the Rectangle object"""
    def __init__(self,width=0, height=0):
        """The initialzation of a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter to retrive the private object attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private object attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to retrive the private object attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private object attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
