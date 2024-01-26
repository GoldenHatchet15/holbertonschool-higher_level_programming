#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensuring both tuples have at least 2 elements, filling missing one with 0
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Adding the first two elements of each tuple
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
