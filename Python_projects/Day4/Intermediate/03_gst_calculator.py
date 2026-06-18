"""
Intermediate Project 3: GST Calculator
Demonstrates Arithmetic Operators.
Clean Code Principles: Constants for tax brackets, descriptive logic.
"""

def calculate_gst_amount(original_price, gst_percentage):
    """Calculates the GST amount based on the given percentage."""
    return original_price * (gst_percentage / 100)

def run_gst_calculator():
    # Standard GST Slabs in some countries (e.g., India)
    GST_SLAB_5 = 5
    GST_SLAB_12 = 12
    GST_SLAB_18 = 18
    GST_SLAB_28 = 28

    print("--- GST Calculator ---")
    
    try:
        item_price = float(input("Enter the base price of the item: $"))
        
        if item_price <= 0:
            print("Price must be greater than zero.")
            return

        print("\\nSelect GST Slab:")
        print(f"1. {GST_SLAB_5}%")
        print(f"2. {GST_SLAB_12}%")
        print(f"3. {GST_SLAB_18}%")
        print(f"4. {GST_SLAB_28}%")
        
        choice = input("Enter choice (1-4): ")
        
        gst_rate = 0
        if choice == '1':
            gst_rate = GST_SLAB_5
        elif choice == '2':
            gst_rate = GST_SLAB_12
        elif choice == '3':
            gst_rate = GST_SLAB_18
        elif choice == '4':
            gst_rate = GST_SLAB_28
        else:
            print("Invalid choice selected.")
            return

        gst_amount = calculate_gst_amount(item_price, gst_rate)
        final_price = item_price + gst_amount # Arithmetic Operator
        
        print(f"\\n--- Billing Details ---")
        print(f"Base Price: ${item_price:.2f}")
        print(f"GST Applied ({gst_rate}%): +${gst_amount:.2f}")
        print(f"Final Price (incl. GST): ${final_price:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    run_gst_calculator()
