#!/usr/bin/python3
for char in range(25, -1, -1):
    s = char + ord('A')
    if char % 2 == 1:
        s += 32
    print("{:c}".format(s), end="")
