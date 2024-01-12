#!/usr/bin/python3
"""
It takes in a URL, sends a request to URL
displays body of response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)

    except requests.HTTPError as err:
        print("Error code: {}".format(err.response.status_code))
