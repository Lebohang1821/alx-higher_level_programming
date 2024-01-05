#!/bin/bash
# It makes PUT request to 0.0.0.0:5000/catch_me with curl
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
