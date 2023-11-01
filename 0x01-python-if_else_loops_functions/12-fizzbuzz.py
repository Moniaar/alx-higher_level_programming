#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0):
            print("Fizz", end=" ")
        elif (x % 5 == 0):
            print("Buzz", end=" ")
        elif (x % 15 == 0):
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(x), end=" ")
