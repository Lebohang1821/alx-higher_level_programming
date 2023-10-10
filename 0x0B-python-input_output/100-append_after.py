#!/usr/bin/python3
"""It defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing given string in file.

    Args:
        filename (str): The name of the file.
        search_string (str): String - search for within file.
        new_string (str): String - insert.
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
