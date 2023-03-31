#! /usr/bin/env python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content_bytes = response.read()
    content_utf8 = content_bytes.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(content_bytes), content_bytes, content_utf8))