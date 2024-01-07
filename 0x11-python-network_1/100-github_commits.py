#!/usr/bin/python3
"""Module that takes your Github credentials (username and password) and uses
the Github API to display your id."""
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except (ValueError, KeyError):
        print("An error occurred while processing the data.")
