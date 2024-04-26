#!/usr/bin/python3
"""Displays the value of the 'X-Request-Id' header from the response of a given URL."""

import requests
import sys

def display_header_value(url):
    # Send a GET request
    response = requests.get(url)
    # Get the 'X-Request-Id' header
    x_request_id = response.headers.get('X-Request-Id')
    # Print the value
    if x_request_id:
        print(x_request_id)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        display_header_value(sys.argv[1])

