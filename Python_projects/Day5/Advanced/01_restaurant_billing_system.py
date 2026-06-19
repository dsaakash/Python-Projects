"""
Advanced Project 1: Restaurant Billing System
Concepts: Nested Lists (Menu), parallel lists (Order/Quantities), list comprehensions.
"""

def display_menu(menu):
    print("\\n--- Restaurant Menu ---")
    for idx, item in enumerate(menu):
        print(f"{idx + 1}. {item[0]:<20} - ${item[1]:.2f}")

def generate_bill(menu, ordered_indices, quantities):
    print("\\n" + "="*30)
    print("       FINAL BILL       ")
    print("="*30)
    
    total = 0.0
    for idx, qty in zip(ordered_indices, quantities):
        item_name = menu[idx][0]
        item_price = menu[idx][1]
        item_total = item_price * qty
        total += item_total
        print(f"{item_name:<15} x{qty:<2} : ${item_total:.2f}")
        
    print("-" * 30)
    print(f"Grand Total: ${total:.2f}")
    print("="*30)

def run_billing():
    # [Name, Price]
    menu = [
        ["Burger", 5.99],
        ["Pizza", 12.99],
        ["Fries", 2.99],
        ["Coke", 1.50],
        ["Ice Cream", 3.50]
    ]
    
    ordered_indices = []
    quantities = []
    
    while True:
        display_menu(menu)
        print("\\n0. Finish Ordering and Generate Bill")
        
        try:
            choice = int(input("Enter item number (0 to finish): "))
            
            if choice == 0:
                break
                
            idx = choice - 1
            if 0 <= idx < len(menu):
                qty = int(input(f"Enter quantity for {menu[idx][0]}: "))
                if qty > 0:
                    ordered_indices.append(idx)
                    quantities.append(qty)
                    print("Added to order.")
                else:
                    print("Quantity must be positive.")
            else:
                print("Invalid item number.")
                
        except ValueError:
            print("Invalid input.")
            
    if ordered_indices:
        generate_bill(menu, ordered_indices, quantities)
    else:
        print("No items ordered.")

if __name__ == "__main__":
    run_billing()
