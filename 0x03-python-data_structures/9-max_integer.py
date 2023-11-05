#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    copy_list = my_list.copy()
    copy_list.sort()
    return copy_list[-1]
