#!/usr/bin/python3
"""It defines function to format text by adding two new lines after each '.', '?', and ':'."""


def format_text(text):
    """It prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): Text to format.
    Raises:
        TypeError: If text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
