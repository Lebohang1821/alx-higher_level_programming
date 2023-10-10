#!/usr/bin/python3
"""Defines a text file writing function."""


def write_text_to_file(filename="", text=""):
    """Write a given text to a UTF-8 encoded file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
