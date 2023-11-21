#!/usr/bin/python3
"""creating a module to handle a square object"""


class Square:
    """Defining the Square object"""
    def __init__(self, size):
        """Definning the first constructor in this class

        Arg:
            size: Length of a one side given from the Square object
        """
        self.__size = size
