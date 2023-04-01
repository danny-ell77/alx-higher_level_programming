#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the
URL and displays the body of the response."""

import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    print(response.json().get("id"))
