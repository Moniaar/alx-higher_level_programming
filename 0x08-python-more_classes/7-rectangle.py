#!/usr/bin/python3
"""creating a module to handle a Rectangle object"""


class Rectangle:
    """Defining the Rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The initialzation of a Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Method to measure and  return the Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to measure and return the rectangle perimeter"""
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Method to create a string of a rectangle"""
        if not self.width or not self.height:
            return " "
        return ((str(self.print_symmbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle to
        be able to recreate a new instance"""
        return "Rectangle(" + str(self.width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """return a string that says Bye rectangle
        everytime an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
