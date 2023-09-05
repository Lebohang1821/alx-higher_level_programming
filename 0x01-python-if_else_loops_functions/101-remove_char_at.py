#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(string, n):
    """Remove the character at position n from the string."""
    if n < 0 or n >= len(string):
        return string
    return string[:n] + string[n+1:]
