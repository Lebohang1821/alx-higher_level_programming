#!/usr/bin/python3
ght_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    de = 0

    for tup in my_list:
        numb += tup[0] * tup[1]
        de += tup[1]

    return (numb / de)
