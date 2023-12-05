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
            raise ValueError("{} must be greater than 0".format(name)

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
