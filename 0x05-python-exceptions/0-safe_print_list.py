#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements to print.

    Returns:
        Number of elements actually printed.
    """
    the_ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=" ")
            the_ret += 1
        except IndexError:
            break
    print("")  # Print a newline after the elements are printed.
    return (the_ret)
