#!/bin/bash
# It takes in URL as argument, sends GET request to URL, and displays body of response
curl -sH 'X-School-User-Id: 98' '$1'
