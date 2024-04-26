#!/usr/bin/python3
"""Sends a POST request to the given URL with an email and displays the response body."""

import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    # Prepare the data to be posted
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    # Create a request object
    req = urllib.request.Request(url, data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        post_email(sys.argv[1], sys.argv[2])

