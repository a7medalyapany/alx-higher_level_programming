#!/usr/bin/python3
"""Module that takes your Github credentials (username and password) and uses
the Github API to display your id."""
import requests
import sys

if __name__ == "__main__":
    RN = sys.argv[1]
    ON = sys.argv[2]

    url = f'https://api.github.com/repos/{ON}/{RN}/commits'

    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except (ValueError, KeyError):
        print("An error occurred while processing the data.")
