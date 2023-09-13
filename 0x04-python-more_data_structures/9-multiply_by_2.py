#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _dir = a_dictionary.copy()
    list_keys = list(_dir.keys())

    for i in list_keys:
        _dir[i] *= 2

    return _dir
