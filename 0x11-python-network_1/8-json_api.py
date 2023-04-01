#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
     q = argv[1] if len(argv) == 2 else ""
     url = 'http://0.0.0.0:5000/search_user'
     req = request.post(url, data={'q':q})
     try:
         req_dict = req.json()
         id, name = req_dict.get('id'), req_dict.get('name')
         if len(req_dict) == 0 or not id or not name:
             print("No result")
         else:
             print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
     except:
         print("Not a valid")
