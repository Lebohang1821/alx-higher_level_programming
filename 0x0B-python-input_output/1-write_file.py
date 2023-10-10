#!/usr/bin/python3
"""It defines file-writing function."""


def write_file(filename="", text=""):
    """Write string to UTF8 text file.

    Args:
        filename (str): Name of file - write.
        text (str): Text - write - file.
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
