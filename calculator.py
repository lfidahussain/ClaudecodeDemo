#!/usr/bin/env python3
"""
Beginner-friendly Python console calculator.
Performs basic arithmetic operations on two numbers with error handling.
"""


def get_valid_number(prompt):
    """Get a valid number input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def get_operation():
    """Get a valid operation from the user."""
    valid_operations = {"+", "-", "*", "/"}
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in valid_operations:
            return operation
        print("Error: Please enter one of the following operations: +, -, *, /")


def calculate(num1, num2, operation):
    """Perform the calculation and return the result."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return num1 / num2


def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("      Welcome to Python Calculator")
    print("=" * 40)

    num1 = get_valid_number("Enter first number: ")
    operation = get_operation()
    num2 = get_valid_number("Enter second number: ")

    try:
        result = calculate(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"\n{e}")


if __name__ == "__main__":
    main()
