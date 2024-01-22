#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            # Try to perform the division
            quotient = my_list_1[i] / my_list_2[i]
            
            # If successful, append the result to the new list
            result.append(quotient)
        
        except ZeroDivisionError:
            # Handle division by zero
            result.append(0)
            print("division by 0")
        
        except TypeError:
            # Handle wrong type
            result.append(0)
            print("wrong type")
        
        except IndexError:
            # Handle out of range
            result.append(0)
            print("out of range")
        
        finally:
            # This block ensures that the loop continues even if an exception occurred
            pass
    
    return result
