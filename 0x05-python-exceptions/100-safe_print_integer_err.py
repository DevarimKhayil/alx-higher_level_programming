#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        # Attempt to print the integer value
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Handle exceptions (ValueError for non-integer values, TypeError for format issues)
        print("Exception: {}".format(e), file=sys.stderr)
        return False

