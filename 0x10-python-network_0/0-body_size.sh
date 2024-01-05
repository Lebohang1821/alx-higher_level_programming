#!/bin/bash
# It sends a request to that URL, and displays size of body - response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
