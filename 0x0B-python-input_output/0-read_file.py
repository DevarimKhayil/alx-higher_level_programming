#!/usr/bin/python3
"""
Module for reading a text file and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        file.read()
        print(file)
