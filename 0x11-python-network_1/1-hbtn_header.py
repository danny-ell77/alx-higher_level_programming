#! /usr/bin/env python3
""" a Python script that takes in a URL, sends a request to the URL and displays 
the value of the X-Request-Id variable found in the header of the response."""

import sys
from urllib import request

url = sys.argv[1]
with request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
    