#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """Prints x elememts of list.

    Args:
        my_list (list): List to print elements from.
        x (int): Num of elements of my_list - print.

    Returns:
        Num of elements printed.
    """
    the_ret = 0
    for l in range(x):
        try:
            print("{}".format(my_list[l]), end="")
            the_ret += 1
        except IndexError:
            break
    print("")
    return (the_ret)
