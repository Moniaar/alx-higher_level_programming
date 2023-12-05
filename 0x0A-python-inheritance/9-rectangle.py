#!/usr/bin/python3
""" A module to create an empty class
named BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a special class for rectangles """
    def __init__(self, width, height):
        """ Initializes a rectangle with the given width and height.

        Args:
            width: width of the rectangle (positive integer)
            height: height of the rectangle (positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Computes and returns the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the rectangle. """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
