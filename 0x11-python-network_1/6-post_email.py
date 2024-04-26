#!/usr/bin/python3
"""Sends a POST request with an email to a specified URL and prints the response."""

import requests
import sys

def send_post_request(url, email):
    # Prepare data payload for POST request
    payload = {'email': email}
    # Send POST request
    response = requests.post(url, data=payload)
    # Print the body of the response
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        send_post_request(sys.argv[1], sys.argv[2])

