#!/bin/bash
# Check if the correct number of arguments is provided

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with curl
curl -s -X POST "$url" -d "email=$email" -d "subject=$subject" | cat

echo ""
