#!/bin/bash
# It sends a DELETE request - URL passed s first argument and displays body of response
curl -s "$1" -X DELETE
