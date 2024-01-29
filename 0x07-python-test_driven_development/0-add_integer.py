#!/usr/bin/python3
"""
This module contains a function that adds two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a (int or float): The first number.
    - b (int or float): The second number (default is 98).

    Returns:
    An integer: The sum of a and b.

    Raises:
    - TypeError: If a or b is not an integer or float.

    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b
