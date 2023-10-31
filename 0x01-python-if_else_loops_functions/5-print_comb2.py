#!/usr/bin/python3
for j in range(100):
    print("{:02d}".format(j), end="\n" if j == 99 else ", ")
