#!/usr/bin/python3
"""creating a module to handle a square object"""


class Square:
    """Defining the Square object"""
    def __init__(self, size=0):
        """Definning the first constructor in this class

        Arg:
            size: Length of a one side given from the Square object

        Raises:
            TypeError: If the size isn't an integer
            ValueError: If the size value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
