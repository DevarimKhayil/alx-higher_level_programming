#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Attempt to execute the provided function with the given arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Handle any exception that occurred during the function execution
        print("Exception: {}".format(e), file=sys.stderr)
        return None
