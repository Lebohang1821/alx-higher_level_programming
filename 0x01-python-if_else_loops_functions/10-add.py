#!/usr/bin/env python3

def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

if __name__ == "__main__":
    num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))
    print(f"The result of adding {num1} and {num2} is: {add_numbers(num1, num2)}")
