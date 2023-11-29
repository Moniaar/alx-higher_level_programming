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

    def __setattr__(self, name, value):
        """Overrides the default attribute setting behavior to allow only
        the attribute 'first_name' to be set.

        Args:
        name (str): The name of the attribute being set.
        value: The value to be assigned to the attribute.

        Raises:
        AttributeError: If an attempt is made to set an attribute other
            than 'first_name'.
        """

        if name != 'first_name':
            raise AttributeError("Can't create new except 'first_name'")
        super().__setattr__(name, value)
