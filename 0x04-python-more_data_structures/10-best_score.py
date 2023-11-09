#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    max_ley = None
    for key, j in a_dictionary.items():
        if j > max_value:
            max_value = j
            max_key = key
    return max_key
