#! /usr/bin/env python3
"""  a Python script that takes in a URL and an email, sends a POST request to the passed URL
 with the email as a parameter, and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request

url = sys.argv[1]
email = sys.argv[2]
with urllib.request.urlopen(url, data={"email": email}) as response:
    print("Your email is: {}".format(response.read().decode("utf-8")))
    