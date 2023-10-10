#!/usr/bin/python3
"""It defines JSON file-reading function."""
import json


def load_from_json_file(filename):
    """It create object from JSON file."""
    with open(filename) as f:
        return json.load(f)
