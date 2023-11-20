#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    k = 0
    try:
        while k is not x:
            print(my_list=[], end='')
            k += 1
    except IndexError:
        None
    print()
    return k
