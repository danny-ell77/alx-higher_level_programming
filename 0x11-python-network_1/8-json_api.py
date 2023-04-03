#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the
URL and displays the body of the response."""

import sys
import requests

if __name__ == "__main__":

    try:
        data = sys.argv[1]
    except IndexError:
        data = None

    payload = {"q": data if data else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
