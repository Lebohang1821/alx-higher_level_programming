#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with "{:d}".format().

    Args:
        value (int): Integer print.

    Returns:
        bool: True if value was printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
