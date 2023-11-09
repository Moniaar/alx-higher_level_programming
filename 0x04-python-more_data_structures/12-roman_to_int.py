#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    nums = 0
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in reversed(roman_string):
        nums = digit[x]
        total += nums if total < nums * 5 else -nums
    return total
