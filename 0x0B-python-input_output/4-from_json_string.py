#!/usr/bin/python3
import json

def from_json_string(my_str):
    """Converts a JSON string to a Python object."""
    return json.loads(my_str)

