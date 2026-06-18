"""
Intermediate Project 4: Swiggy Bill Generator
Demonstrates Arithmetic, Assignment, and Logical Operators.
Clean Code Principles: Extracted fee logic, meaningful variable names.
"""

def calculate_delivery_fee(distance_km):
    """Calculates delivery fee based on distance."""
    BASE_FEE = 20.0 # Standard currency units
    EXTRA_FEE_PER_KM = 5.0
    FREE_DELIVERY_DISTANCE = 2.0
    
    if distance_km <= FREE_DELIVERY_DISTANCE:
        return BASE_FEE
        
    extra_distance = distance_km - FREE_DELIVERY_DISTANCE
    return BASE_FEE + (extra_distance * EXTRA_FEE_PER_KM)

def calculate_packing_charges(item_count):
    """Fixed packing charge per item."""
    PACKING_CHARGE_PER_ITEM = 10.0
    return item_count * PACKING_CHARGE_PER_ITEM

def run_swiggy_bill_generator():
    print("--- Swiggy Bill Generator ---")
    
    total_food_cost = 0.0
    item_count = 0
    
    while True:
        try:
            item_price = float(input("Enter food item price (or 0 to finish adding): $"))
            if item_price == 0:
                break
            if item_price < 0:
                print("Price cannot be negative.")
                continue
                
            total_food_cost += item_price # Assignment operator
            item_count += 1
            
        except ValueError:
            print("Invalid price. Please enter a number.")
            
    if item_count == 0:
        print("No items added. Exiting.")
        return
        
    try:
        distance = float(input("\\nEnter delivery distance in km: "))
        
        delivery_fee = calculate_delivery_fee(distance)
        packing_charges = calculate_packing_charges(item_count)
        
        # Surge pricing logic (Logical and Comparison Operators)
        is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'
        surge_fee = 30.0 if is_raining else 0.0
        
        grand_total = total_food_cost + delivery_fee + packing_charges + surge_fee
        
        print("\\n--- Final Bill Summary ---")
        print(f"Food Total ({item_count} items): ${total_food_cost:.2f}")
        print(f"Packing Charges: ${packing_charges:.2f}")
        print(f"Delivery Fee: ${delivery_fee:.2f}")
        if surge_fee > 0:
            print(f"Surge Pricing (Rain): +${surge_fee:.2f}")
        print(f"---------------------------")
        print(f"Grand Total to Pay: ${grand_total:.2f}")
        
    except ValueError:
        print("Invalid input for distance.")

if __name__ == "__main__":
    run_swiggy_bill_generator()
