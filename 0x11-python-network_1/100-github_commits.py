#!/usr/bin/python3
"""Lists the last 10 commits of a given repository and owner."""

import requests
import sys

def list_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        list_commits(sys.argv[1], sys.argv[2])

