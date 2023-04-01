#!/bin/python3
"""A script that fetches
   https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')as response:
        webContent = response.read()
        print("Body request:")
        print("\t- type: {}".format(type(webContent)))
        print("\t- content: {}".format(webContent))
        print("\t- utf8 content: {}".format(webContent.decode('utf-8')))
