#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """
    This script prints all non-private names defined in the hidden_4 module.
    """
    names = dir(hidden_4)
    for name_ in names:
        if not name_.startswith("__"):
            print(name_)
