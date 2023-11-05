#!/usr/bin/python3
def no_c(my_string):
    back = ""
    for j in range(len(my_string)):
        if (my_string[j] != 'c' and my_string[j] != 'C'):
            back += my_string[j]
    return back
