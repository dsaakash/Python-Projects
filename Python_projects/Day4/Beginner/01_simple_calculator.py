"""
Beginner Project 1: Simple Calculator
Demonstrates Arithmetic Operators.
Clean Code Principles: Meaningful names, small functions.
"""

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def display_menu():
    print("\\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("-------------------------")

def run_calculator():
    display_menu()
    
    try:
        choice = int(input("Select operation (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid selection. Please run again.")
            return

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == 1:
            result = add_numbers(first_number, second_number)
            print(f"Result: {first_number} + {second_number} = {result}")
        elif choice == 2:
            result = subtract_numbers(first_number, second_number)
            print(f"Result: {first_number} - {second_number} = {result}")
        elif choice == 3:
            result = multiply_numbers(first_number, second_number)
            print(f"Result: {first_number} * {second_number} = {result}")
        elif choice == 4:
            result = divide_numbers(first_number, second_number)
            print(f"Result: {first_number} / {second_number} = {result}")

    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    run_calculator()
