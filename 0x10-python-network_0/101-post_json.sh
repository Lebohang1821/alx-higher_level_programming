#!/bin/bash
# It sends JSON POST request - URL passed as first argument, and displays body of response
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
