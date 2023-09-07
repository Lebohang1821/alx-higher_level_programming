#!/usr/bin/python3

def magic_calculation(a, b):
    """Perform a custom magic calculation based on the values of 'a' and 'b'.
    
    If 'a' is less than 'b', it adds 'a' and 'b' and then adds numbers from 4 to 5.
    Otherwise, it subtracts 'b' from 'a'.

    :param a: An integer value.
    :param b: An integer value.
    :return: The result of the magic calculation.
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return sub(a, b)
