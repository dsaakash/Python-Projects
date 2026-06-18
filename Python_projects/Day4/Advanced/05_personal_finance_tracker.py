"""
Advanced Project 5: Personal Finance Tracker
Demonstrates all operator types combined in a functional loop.
Clean Code Principles: Modularity, clean console UI, robust error handling.
"""

def add_transaction(balance, is_income):
    trans_type = "Income" if is_income else "Expense"
    try:
        amount = float(input(f"Enter {trans_type} amount: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance
            
        if is_income:
            balance += amount
            print(f"Income of ${amount:.2f} recorded.")
        else:
            if amount > balance:
                print("Warning: This expense exceeds your current balance!")
            balance -= amount
            print(f"Expense of ${amount:.2f} recorded.")
            
        return balance
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return balance

def check_financial_status(balance, target_savings):
    if balance >= target_savings:
        print("Status: Excellent! You have met or exceeded your savings target.")
    elif balance > 0:
        shortfall = target_savings - balance
        print(f"Status: Good. You are ${shortfall:.2f} away from your target.")
    else:
        print("Status: Critical! You are in debt. Please review your expenses.")

def run_finance_tracker():
    print("--- Personal Finance Tracker ---")
    
    try:
        balance = float(input("Enter starting bank balance: $"))
        target_savings = float(input("Enter your savings goal: $"))
    except ValueError:
        print("Invalid starting values. Exiting.")
        return

    while True:
        print(f"\\n--- Current Balance: ${balance:.2f} ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Check Goal Status")
        print("4. Exit")
        
        choice = input("Select an action (1-4): ")
        
        if choice == '1':
            balance = add_transaction(balance, is_income=True)
        elif choice == '2':
            balance = add_transaction(balance, is_income=False)
        elif choice == '3':
            check_financial_status(balance, target_savings)
        elif choice == '4':
            print("Exiting Tracker. Have a financially healthy day!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    run_finance_tracker()
