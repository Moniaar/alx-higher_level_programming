#!/usr/bin/python3
"""This is a remarkable module """


import json


def save_to_json_file(my_obj, filename):
    """A function to write an Object to a text file,
    using a JSON representation """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dumps(my_obj, f)
