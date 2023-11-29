#!/usr/bin/python3
"""Making a module that contains a class"""


class LockedClass:
    """A class that prevents the dynamic creation of new instance attributes,
    except for the attribute 'first_name'.

    Attributes:
    __slots__ (tuple): A tuple specifying the allowed attribute names.

    Methods:
    __setattr__(self, name, value): Overrides the default attribute setting
        behavior to allow only the attribute 'first_name' to be set."""
    __slots__ = ('first_name',)
