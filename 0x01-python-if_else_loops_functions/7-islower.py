#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check for lowercase characters."""
    if len(c) == 1 and c.islower():
        return True
    else:
        return False
