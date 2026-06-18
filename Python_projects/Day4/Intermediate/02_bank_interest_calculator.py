"""
Intermediate Project 2: Bank Interest Calculator
Demonstrates Arithmetic Operators (Simple & Compound Interest).
Clean Code Principles: Clear variable names, separate calculation logic.
"""

def calculate_simple_interest(principal, rate_percent, time_years):
    """Calculates Simple Interest: (P * R * T) / 100"""
    return (principal * rate_percent * time_years) / 100

def calculate_compound_interest(principal, rate_percent, time_years, compound_frequency=1):
    """
    Calculates Compound Interest.
    A = P (1 + r/n)^(nt)
    """
    rate_decimal = rate_percent / 100
    amount = principal * ((1 + (rate_decimal / compound_frequency)) ** (compound_frequency * time_years))
    interest = amount - principal
    return interest

def run_interest_calculator():
    print("--- Bank Interest Calculator ---")
    
    try:
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (in years): "))
        
        if principal < 0 or rate < 0 or time < 0:
            print("Values cannot be negative.")
            return

        print("\\n--- Interest Calculation Types ---")
        print("1. Simple Interest")
        print("2. Compound Interest (Annually)")
        
        choice = input("Select calculation type (1/2): ")
        
        if choice == '1':
            interest = calculate_simple_interest(principal, rate, time)
            print(f"\\nSimple Interest Earned: ${interest:.2f}")
            print(f"Total Amount: ${principal + interest:.2f}")
            
        elif choice == '2':
            interest = calculate_compound_interest(principal, rate, time)
            print(f"\\nCompound Interest Earned: ${interest:.2f}")
            print(f"Total Amount: ${principal + interest:.2f}")
            
        else:
            print("Invalid selection.")

    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    run_interest_calculator()
