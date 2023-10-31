#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char != ord('e') and char != ord('q'):
        print("{:c}".format(char), end="")
