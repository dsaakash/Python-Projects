"""
Intermediate Project 1: ATM Balance Checker
Demonstrates Logical, Comparison, and Assignment Operators.
Clean Code Principles: Small functions, single responsibility.
"""

def withdraw_amount(balance, amount):
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return balance
        
    if amount > balance:
        print("Insufficient funds! Transaction declined.")
        return balance
        
    balance -= amount # Assignment operator
    print(f"Successfully withdrew ${amount:.2f}")
    return balance

def deposit_amount(balance, amount):
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return balance
        
    balance += amount
    print(f"Successfully deposited ${amount:.2f}")
    return balance

def run_atm():
    print("--- Welcome to the ATM ---")
    
    # Initialize with some dummy balance
    current_balance = 500.00
    
    # Simple PIN verification (Logical and Comparison)
    PIN = "1234"
    attempts = 3
    is_authenticated = False
    
    while attempts > 0 and not is_authenticated:
        entered_pin = input(f"Enter PIN ({attempts} attempts left): ")
        if entered_pin == PIN:
            is_authenticated = True
        else:
            attempts -= 1
            print("Incorrect PIN.")
            
    if not is_authenticated:
        print("Account locked. Please contact your bank.")
        return

    while True:
        print(f"\\nCurrent Balance: ${current_balance:.2f}")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                withdraw_val = float(input("Enter amount to withdraw: $"))
                current_balance = withdraw_amount(current_balance, withdraw_val)
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            try:
                deposit_val = float(input("Enter amount to deposit: $"))
                current_balance = deposit_amount(current_balance, deposit_val)
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    run_atm()
