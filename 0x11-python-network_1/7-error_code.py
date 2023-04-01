#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL 
and displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    status = req.status_code
    print(req.text) if status < 400 else print(
        "Error code: {}".format(status))
