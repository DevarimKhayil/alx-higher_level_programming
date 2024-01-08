#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use 0 for each missing integer
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Use only the first 2 integers if a tuple is bigger than 2
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
