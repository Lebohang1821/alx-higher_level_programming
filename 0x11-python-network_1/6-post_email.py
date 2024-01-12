#!/usr/bin/python3
'''
It takes in a URL and an email address
sends POST request to passed URL with email as parameter
Finally displays body of response.
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
