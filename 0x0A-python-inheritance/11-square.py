#!/usr/bin/python3
""" A module to create an empty class
named BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to define a small square"""
    def __init__(self, size):
        """a function to hide the size and get it """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area of square'''
        return self.__size ** 2

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
