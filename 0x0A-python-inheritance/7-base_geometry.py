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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
