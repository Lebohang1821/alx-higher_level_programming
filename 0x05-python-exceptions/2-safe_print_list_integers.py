#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of list that are integers.

    Args:
        my_list (list): List to print elements from.
        x (int): Numb of elements of my_list to print.

    Returns:
        Num of elements printed.
    """
    ret_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret_elements += 1
        except (ValueError, TypeError):
            pass
    print()
    return (ret_elements)
