"""
Advanced Project 1: Profit Loss Calculator
Demonstrates Arithmetic, Comparison, and Logical Operators.
Clean Code Principles: Comprehensive handling of edge cases, modular logic.
"""

def calculate_financials(cost_price, selling_price, units_sold):
    total_cost = cost_price * units_sold
    total_revenue = selling_price * units_sold
    difference = total_revenue - total_cost
    return total_cost, total_revenue, difference

def run_profit_loss():
    print("--- Business Profit & Loss Calculator ---")
    
    try:
        cost_price = float(input("Enter Cost Price per unit: $"))
        selling_price = float(input("Enter Selling Price per unit: $"))
        units_sold = int(input("Enter number of units sold: "))
        
        if cost_price < 0 or selling_price < 0 or units_sold < 0:
            print("Values cannot be negative.")
            return

        total_cost, total_revenue, difference = calculate_financials(cost_price, selling_price, units_sold)
        
        print(f"\\n--- Financial Summary ---")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        
        # Logical / Comparison operators
        if difference > 0:
            profit_margin = (difference / total_cost) * 100
            print(f"Result: Profit of ${difference:.2f}")
            print(f"Profit Margin: {profit_margin:.2f}%")
        elif difference < 0:
            loss = abs(difference)
            loss_percent = (loss / total_cost) * 100
            print(f"Result: Loss of ${loss:.2f}")
            print(f"Loss Percentage: {loss_percent:.2f}%")
        else:
            print("Result: Break-even (No Profit, No Loss)")
            
    except ValueError:
        print("Invalid input! Please enter numbers.")
        
if __name__ == "__main__":
    run_profit_loss()
