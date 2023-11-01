#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for j, char in enumerate(str):
        if j != n:
            new += char
    return new
