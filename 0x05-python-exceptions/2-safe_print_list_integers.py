#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j, k = 0, 0
    while j < x:
        try:
            print("{:d}".format(my_list[j]), end='')
            k += 1
        except (ValueError, TypeError):
            pass
        j += 1
    print()
    return k
