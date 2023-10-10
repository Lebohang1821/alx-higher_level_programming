#!/usr/bin/python3
"""It efines file-appending function."""


def append_write(filename="", text=""):
    """Appends string - end of UTF8 text file.

    Args:
        filename (str): Name of file to append to.
        text (str): String - append - file.
    Returns:
        umber characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
