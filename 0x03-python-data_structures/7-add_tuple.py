#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = tuple_a[0] if len(tuple_a) > 0 else 0
    x2 = tuple_a[1] if len(tuple_a) > 1 else 0
    y1 = tuple_b[0] if len(tuple_b) > 0 else 0
    y2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (x1 + y1, x2 + y2)
