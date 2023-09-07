#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total_nu = 0
    for i in range(1, len(sys.argv)):
        total_nu += int(sys.argv[i])
    print(total_nu)
