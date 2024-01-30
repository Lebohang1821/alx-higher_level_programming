#!/bin/bash
# It just check if correct number of arguments is provided
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
