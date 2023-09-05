#!/usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    result = ""
    for c in input_str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
        print(result)
