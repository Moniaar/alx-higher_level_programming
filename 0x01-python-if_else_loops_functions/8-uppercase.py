#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}"
                .format(ord(c) if not islower(c) else ord(c) - 32),
                end="")
        print("")

