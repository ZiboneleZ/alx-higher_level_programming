#!/usr/bin/python3
"""
script that takes your GitHub credentials 
(username and password) 
and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == '__name__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    req = request.get(url, auth=info)
    try:
        print(req.json()['id'])
    except Exception:
        print('None')
