# def new_in_list(my_list, idx, element):
#   if idx < 0 or idx >= len(my_list):
#       return my_list
#   new_list = copy.deepcopy(my_list)
#   new_list[idx] = new_element
#  return new_list
#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Replace the element at the specified index in the new list
    new_list[idx] = element
    
    return new_list
