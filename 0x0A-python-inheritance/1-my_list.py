#!/usr/bin/python3
"""importing new module in here"""


class MyList(list):
    """a class from List type"""
    def print_sorted(self):
        """ A method that prints the list,
        but sorted (ascending sort)

        Args:
            self: a passed defalut parameters
        """
        sorted_list = sorted(self)
        print(sorted_list)
