#!/bin/python3
"""
 script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

import sys
import requests

if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    repository_info = repository_name + "/" + owner_name
    url = "https://api.github.com/repos/" + repository_info + "/commits"
    req = requests.get(url)
    top = req.json()[:10]
    for i in top:
        el = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(el, author))
