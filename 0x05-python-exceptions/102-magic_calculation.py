#!/usr/bin/python3


def magic_calculation(a, b):
    eq_to = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                eq_to += a ** b / x
        except:
            eq_to = b + a
            break
    return (eq_to)
