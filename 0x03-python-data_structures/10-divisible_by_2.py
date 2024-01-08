#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store True or False for each element in my_list
    result_list = []

    # Iterate through each element in my_list
    for num in my_list:
        # Check if the element is divisible by 2
        result_list.append(num % 2 == 0)

    return result_list
