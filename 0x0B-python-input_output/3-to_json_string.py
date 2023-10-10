#!/usr/bin/python3
"""It defines string-to-JSON function"""
import json


def to_json_string(my_obj):
    """It return JSON representation - string object"""
    return json.dumps(my_obj)
