#!/usr/bin/python3
"""
It takes 2 arguments in order to solve this challenge
The first argument will be repository name
second argument will be owner name
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
