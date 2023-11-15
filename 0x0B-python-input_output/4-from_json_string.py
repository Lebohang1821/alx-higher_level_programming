#!/usr/bin/python3
"""It defines JSON-to-object function"""
import json


def from_json_string(my_str):
    """It is a representation of JSON string"""
    return json.loads(my_str)
