#!/usr/bin/python3
"""
Module for the MyInt class.
"""

class MyInt(int):
    """
    Class representing a rebel integer.

    Inherits from int and inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: The result of the inverted == operator.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: The result of the inverted != operator.

        """
        return super().__eq__(other)

