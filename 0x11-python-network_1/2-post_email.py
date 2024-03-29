#!/usr/bin/python3
"""  a Python script that takes in a URL
and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    with request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
