#!/usr/bin/python3
"""Fetches status from ALX intranet URL using requests and displays the response."""

import requests

def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text  # Response content as a Python string

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")

if __name__ == "__main__":
    fetch_status()

