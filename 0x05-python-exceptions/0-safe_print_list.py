#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements of my_list to print.

    Returns:
        Number of elements printed
    """
    retur = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            retur += 1
        except IndexError:
            break
    print("")
    return (retur)
