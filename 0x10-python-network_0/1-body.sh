#!/bin/bash
# It takes in URL, sends GET request to URL, and displays body of response
curl -sfL "$1" -X GET | ( [ "$(curl -sw '%{http_code}' "$1")" == "200" ] && cat )
