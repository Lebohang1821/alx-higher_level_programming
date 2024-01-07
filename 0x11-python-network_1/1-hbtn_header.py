#!/usr/bin/python3
"""
It Python script that takes in a URL, sends request to URL 
and displays value of X-Request-Id variable found in header of response
"""
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
except urllib.error.URLError as e:
    print("Error:", e.reason)
