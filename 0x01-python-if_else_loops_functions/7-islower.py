#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check for lowercase characters."""
    if len(c) == 0:
        return "upper"
    elif len(c) == 1 and c.isalpha():
        return "lower" if c.islower() else "upper"
    else:
        return "invalid"
