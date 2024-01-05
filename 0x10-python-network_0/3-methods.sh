#!/bin/bash
# It takes in URL and displays all HTTP methods server will accept
curl -sI $url | grep -i Allow | cut -d' ' -f2-

