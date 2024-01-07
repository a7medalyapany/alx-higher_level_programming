#!/usr/bin/python3
"""Module that takes your Github credentials (username and password) and uses
the Github API to display your id."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data['id'])
    except (ValueError, KeyError):
        print("None")
