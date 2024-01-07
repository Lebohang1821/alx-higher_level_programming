#!/usr/bin/python3
"""
It takes in URL and an email, sends a POST
request to passed URL with email
as a parameter, and displays body of response
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.URLError as e:
    print("Error:", e.reason)
