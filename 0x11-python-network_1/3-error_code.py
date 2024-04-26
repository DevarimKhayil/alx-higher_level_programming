#!/usr/bin/python3
"""Sends a GET request to a given URL and handles potential HTTP errors by displaying the error code."""

import urllib.request
import urllib.error
import sys

def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])

