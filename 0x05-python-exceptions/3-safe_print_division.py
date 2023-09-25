#!/usr/bin/python3

def safe_print_division(a, b):
    """It returns division of a by b."""
    div = None

    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
        div = a / b

    print("Inside result: {}".format(div))
    return (div)
