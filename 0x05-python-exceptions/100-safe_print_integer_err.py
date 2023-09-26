#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
       Print integer with a "{:d}".format().

    If ValueError mesage is caught, corresponding
    message is printed - standard error.

    Args:
        value (int): Integer - print.

    Returns:
        If TypeError or ValueError occurs - False
        Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
