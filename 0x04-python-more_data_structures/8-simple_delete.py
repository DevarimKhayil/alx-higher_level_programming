#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # Check if the key exists in the dictionary
        del a_dictionary[key]  # Delete the key-value pair if the key exists
    return a_dictionary
