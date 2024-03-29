#!/usr/bin/python3
"""
Module for the BaseGeometry class.
"""


class BaseGeometry:
    """
    Class representing a base geometry.

    Public instance methods:
    - area(): Raises an Exception with the message 'area() is not implemented'.
    - integer_validator(name, value): Validates the value.

    Attributes:
    - __name (str): The name of the attribute.
    - __value (int): The value to be validated.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always raises an Exception.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the attribute.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

