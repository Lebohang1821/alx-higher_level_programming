#!/usr/bin/python3
"""
It takes in a URL and an email address
sends POST request to passed URL with email as parameter
Finally displays body of response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    print("Your email is:", email)

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
