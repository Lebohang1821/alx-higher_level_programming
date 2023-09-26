#!/usr/bin/python3


def magic_calculation(a, b):
    eq_to = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                eq_to += a ** b / i
        except:
            eq_to = b + a
            break
    return (eq_to)
