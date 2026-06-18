"""
Advanced Project 4: Startup Burn Rate Calculator
Demonstrates Arithmetic, Assignment, and Logical Operators.
Clean Code Principles: Breaking down expenses, runway calculation.
"""

def get_total_expenses():
    total = 0.0
    categories = ['Salaries', 'Rent', 'Marketing', 'Software Subscriptions', 'Other']
    
    print("Enter Monthly Expenses:")
    for category in categories:
        while True:
            try:
                expense = float(input(f"{category}: $"))
                if expense < 0:
                    print("Expense cannot be negative.")
                    continue
                total += expense # Assignment operator
                break
            except ValueError:
                print("Invalid input.")
    return total

def calculate_runway(cash_balance, monthly_burn_rate):
    if monthly_burn_rate <= 0:
        return float('inf') # Infinite runway if no burn
    return cash_balance / monthly_burn_rate

def run_burn_rate_calculator():
    print("--- Startup Burn Rate & Runway Calculator ---")
    
    try:
        cash_balance = float(input("Enter current cash balance (in bank): $"))
        monthly_revenue = float(input("Enter average monthly revenue: $"))
        
        print("")
        total_monthly_expenses = get_total_expenses()
        
        # Net Burn Rate = Expenses - Revenue
        net_burn_rate = total_monthly_expenses - monthly_revenue
        
        print("\\n--- Financial Health ---")
        print(f"Gross Burn Rate (Total Expenses): ${total_monthly_expenses:.2f}/month")
        
        if net_burn_rate > 0:
            print(f"Net Burn Rate: ${net_burn_rate:.2f}/month (Losing Money)")
            runway_months = calculate_runway(cash_balance, net_burn_rate)
            print(f"Estimated Runway: {runway_months:.1f} months")
            
            if runway_months < 6:
                print("WARNING: Dangerously low runway. Consider fundraising or cutting costs immediately.")
        elif net_burn_rate < 0:
            print(f"Net Income: ${abs(net_burn_rate):.2f}/month (Profitable!)")
            print("Runway: Infinite (You are cash-flow positive)")
        else:
            print("Break-even: You are spending exactly what you earn.")
            print("Runway: Infinite (If conditions remain constant)")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    run_burn_rate_calculator()
