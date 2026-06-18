"""
Beginner Project 8: Pocket Money Tracker
Demonstrates Assignment Operators and Comparison Operators.
Clean Code Principles: Small loop structure, meaningful names.
"""

def process_expense(current_balance, expense_amount):
    """Subtracts expense from balance if sufficient funds exist."""
    if expense_amount > current_balance:
        print("Error: Insufficient funds for this expense.")
        return current_balance
    
    current_balance -= expense_amount # Assignment operator
    return current_balance

def run_pocket_money_tracker():
    print("--- Pocket Money Tracker ---")
    
    try:
        pocket_money = float(input("Enter total pocket money received: $"))
        balance = pocket_money
        
        while balance > 0:
            print(f"\\nCurrent Balance: ${balance:.2f}")
            user_input = input("Enter expense amount (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                break
                
            expense = float(user_input)
            if expense <= 0:
                print("Expense must be greater than zero.")
                continue
                
            balance = process_expense(balance, expense)
            
        print("\\n--- End of Tracking ---")
        print(f"Starting Pocket Money: ${pocket_money:.2f}")
        print(f"Remaining Balance: ${balance:.2f}")
        
        if balance == 0:
            print("Warning: You have run out of pocket money!")
            
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    run_pocket_money_tracker()
