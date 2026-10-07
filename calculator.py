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

# --- Individual operation functions ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return x / y

def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("      Welcome to Python Calculator")
    print("=" * 40)

    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")
    operation = get_operation()

    try:
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        print(f"\nResult: {num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"\n{e}")

if __name__ == "__main__":
    main()



'''

*Demo

Enter first number: 12
Enter second number: 4
Enter operation (+, -, *, /): *
Result: 12.0 * 4.0 = 48.0



Enter first number: 10
Enter second number: 0
Enter operation (+, -, *, /): /
Error: Cannot divide by zero.


'''