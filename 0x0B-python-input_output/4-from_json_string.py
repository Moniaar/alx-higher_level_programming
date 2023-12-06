#!/usr/bin/python3
"""my first module to handle JSON ever"""

import json


def from_json_string(my_str):
    """a function that returns an object (Python
    data structure) represented by a JSON string,
    solving with loads since the object is ready"""
    return json.loads(my_str)
