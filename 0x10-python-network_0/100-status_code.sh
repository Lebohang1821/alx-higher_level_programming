#!/bin/bash
# It sends request - URL passed as argument, and displays only tatus code of response
curl -s -o /dev/null -w '%{http_code}' '$1'
