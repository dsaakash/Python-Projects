"""
Beginner Project 10: Fuel Cost Calculator
Demonstrates Arithmetic Operators.
Clean Code Principles: Extracted formulas, clear variables.
"""

def calculate_fuel_needed(distance_km, mileage_kmpl):
    """Calculates fuel required for a journey."""
    if mileage_kmpl <= 0:
        return 0
    return distance_km / mileage_kmpl

def calculate_total_cost(fuel_needed_liters, fuel_price_per_liter):
    """Calculates the total cost of the fuel."""
    return fuel_needed_liters * fuel_price_per_liter

def run_fuel_calculator():
    print("--- Fuel Cost Calculator ---")
    
    try:
        distance = float(input("Enter trip distance in kilometers: "))
        mileage = float(input("Enter vehicle mileage (km per liter): "))
        fuel_price = float(input("Enter current fuel price per liter: $"))
        
        if distance <= 0 or mileage <= 0 or fuel_price <= 0:
            print("All values must be positive numbers greater than zero.")
            return

        fuel_required = calculate_fuel_needed(distance, mileage)
        total_cost = calculate_total_cost(fuel_required, fuel_price)
        
        print("\\n--- Trip Details ---")
        print(f"Distance: {distance} km")
        print(f"Fuel Required: {fuel_required:.2f} Liters")
        print(f"Estimated Total Cost: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    run_fuel_calculator()
