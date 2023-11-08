#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda j: replace if j == search else j, my_list))
