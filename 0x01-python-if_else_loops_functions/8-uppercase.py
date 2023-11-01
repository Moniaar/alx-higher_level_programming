#!/usr/bin/python3
def islower(c):
    if (ord(c) >= ord('a') and ord(c) <= ord('z')):
        return True
    else:
        return False

def uppercase(str):
    for char in str:
        print("{:c}"
                .format(ord(char) if not islower(char) else ord(char) - 32),
                end="")
    print("")

