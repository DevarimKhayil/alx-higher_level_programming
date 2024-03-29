#!/usr/bin/python3
"""
Module for the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.

        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representation of the Square.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

