#!/usr/bin/python3

import sys

def main():
    """Print the number of and list of arguments."""
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    
    for i in range(count):
        print(f"{i + 1}: {sys.argv[i + 1]}")

if __name__ == "__main__":
    main()
