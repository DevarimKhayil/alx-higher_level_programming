#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable from the response header of a given URL."""

import urllib.request
import sys

def display_header(url):
    with urllib.request.urlopen(url) as response:
        # Retrieve the header value for 'X-Request-Id'
        header_value = response.getheader('X-Request-Id')
        if header_value:
            print(header_value)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        display_header(sys.argv[1])

