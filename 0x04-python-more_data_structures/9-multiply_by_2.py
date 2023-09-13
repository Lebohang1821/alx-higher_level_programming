#!/usr/bin/python3
def multiply_dict_values_by_2(input_dict):
    result_dict = {key: value * 2 for key, value in input_dict.items()}
    return result_dict
