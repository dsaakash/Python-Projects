"""
Beginner Project 5: Grocery Bill Calculator
Demonstrates Arithmetic Operators and Logic.
Clean Code Principles: Meaningful variables, small focused functions.
"""

def apply_discount(total_amount, discount_percentage):
    discount_amount = total_amount * (discount_percentage / 100)
    return total_amount - discount_amount

def calculate_grocery_bill():
    print("--- Grocery Bill Calculator ---")
    
    total_bill = 0.0
    items_count = 0
    
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
            
        try:
            item_price = float(input(f"Enter price of {item_name}: $"))
            item_quantity = int(input(f"Enter quantity of {item_name}: "))
            
            item_total = item_price * item_quantity
            total_bill += item_total # Assignment Operator
            items_count += item_quantity
            print(f"Added: {item_name} x{item_quantity} = ${item_total:.2f}\\n")
            
        except ValueError:
            print("Invalid input for price or quantity. Try again.")

    print("\\n--- Final Bill ---")
    print(f"Total Items: {items_count}")
    print(f"Subtotal: ${total_bill:.2f}")

    # Comparison and Logical Operators
    if total_bill > 100:
        DISCOUNT_RATE = 10 # 10% discount for orders over $100
        discounted_bill = apply_discount(total_bill, DISCOUNT_RATE)
        print(f"Discount Applied ({DISCOUNT_RATE}%): -${total_bill - discounted_bill:.2f}")
        print(f"Final Amount to Pay: ${discounted_bill:.2f}")
    else:
        print(f"Final Amount to Pay: ${total_bill:.2f}")
        print("Spend over $100 to get a 10% discount next time!")

if __name__ == "__main__":
    calculate_grocery_bill()
