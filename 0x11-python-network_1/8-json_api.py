#!/usr/bin/python3
"""Sends a POST request to a given URL with a letter as a parameter and processes the JSON response."""

import requests
import sys

def search_api(letter):
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    try:
        response = requests.post(url, data=data)
        response_json = response.json()  # Attempt to decode the JSON response
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:  # This occurs if the response body is not JSON-decodable
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_api(letter)

