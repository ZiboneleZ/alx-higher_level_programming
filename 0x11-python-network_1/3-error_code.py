#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL 
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys

if __name__ == "__main__":
    
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
        
              
