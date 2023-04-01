#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
