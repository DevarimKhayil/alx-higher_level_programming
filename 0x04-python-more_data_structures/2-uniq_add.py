#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for num in my_list:
        unique_integers.add(num)

    # Sum all unique integers in the set
    sum_unique = sum(unique_integers)
    
    return sum_unique
