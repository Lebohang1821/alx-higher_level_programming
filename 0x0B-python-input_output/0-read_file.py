#!/usr/bin/python3
"""It defines text file-reading function."""


def read_file(filename=""):
    """It print contents of UTF8 text file - stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
