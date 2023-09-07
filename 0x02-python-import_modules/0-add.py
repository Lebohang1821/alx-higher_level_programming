#!/usr/bin/python3

def main():
    """Print the sum of 1 and 2."""
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()
