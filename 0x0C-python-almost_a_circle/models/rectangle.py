#!/usr/bin/python3
"""A module to work with the base class"""
from models.base import Base


class Rectangle(Base):
    """defining a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of this class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """the given first paramaeter for this class"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """the seconed paramaeter for this class"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, type_equality=True):
        """Method for validating integer values entred by the user"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if type_equality and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not type_equality and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """this method calculate the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """returns the area value of the Rectangle instance"""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """assigns a key/value argument to attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update the attributes using keyword arguments"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
