#!/usr/bin/python3
"""Fetches status from an ALX intranet URL using urllib."""

import urllib.request

def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()

