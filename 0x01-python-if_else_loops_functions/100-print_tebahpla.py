#!/usr/bin/python3
# 100-print_tebahpla.py

for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        print(chr(c), end="")
    else:
        print(chr(c).upper(), end="")
