#! /usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_bytes = response.read()
        content_utf8 = content_bytes.decode('utf-8')
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(content_bytes), content_bytes, content_utf8))