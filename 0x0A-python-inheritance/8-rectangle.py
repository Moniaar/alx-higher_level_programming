#!/usr/bin/python3
""" A module to create an empty class
named BaseGeometry """


class BaseGeometry:
    """ An empty class """

    def area(self):
        """ a Function to print the area

        Args:
            self: a given default parameter
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function is to see if your int is valid or not

        Args:
            name: a given name for the value maybe
            value: an integer value most probably
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
