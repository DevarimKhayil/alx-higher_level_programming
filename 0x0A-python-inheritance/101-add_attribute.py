#!/usr/bin/python3
"""
Module for the add_attribute function.
"""

def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr (str): The attribute name.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

