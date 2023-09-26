#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
       Execute function safely.

    Args:
        fct: Function - execute.
        args: Arguments for fct.

    Returns:
        If error occurs - None.
        Otherwise - esult of call to fct.
    """
    try:
        eq_to = fct(*args)
        return (eq_to)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
