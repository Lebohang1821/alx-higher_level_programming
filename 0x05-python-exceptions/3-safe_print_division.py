#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides two integers and prints the result."""
    try:
        _div = a / b
    except ZeroDivisionError:
        _div = None
    finally:
        print("Inside result: {}".format(_div))
    return (_div)
