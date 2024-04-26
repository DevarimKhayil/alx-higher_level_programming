#!/usr/bin/python3
"""Fetches GitHub user ID using GitHub API and basic authentication."""

import requests
import sys

def fetch_github_id(username, token):
    url = f"https://api.github.com/user"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        fetch_github_id(sys.argv[1], sys.argv[2])

