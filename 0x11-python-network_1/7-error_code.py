#!/usr/bin/python3
"""Fetches a URL and prints the body of the response or an error code if the response status code is >= 400."""

import requests
import sys

def fetch_url(url):
    # Send a GET request
    response = requests.get(url)
    # Check the status code for error handling
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])

