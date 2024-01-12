#!/usr/bin/python3
'''
It takes in a URL, sends a request to URL
--displays value of variable X-Request-Id in response header
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
