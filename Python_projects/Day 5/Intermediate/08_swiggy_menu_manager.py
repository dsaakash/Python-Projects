"""
Intermediate Project 8: Swiggy Menu Manager
Concepts: Two parallel lists vs nested lists, list aggregation.
"""

def display_app_menu(items, prices):
    print("\\n--- Current Available Items ---")
    # Using zip() to iterate through two parallel lists simultaneously
    for idx, (item, price) in enumerate(zip(items, prices)):
        print(f"{idx + 1}. {item:<20} - ${price:.2f}")

def run_swiggy_manager():
    # Managing data using two parallel lists (Alternative to nested lists)
    items = ["Burger", "Pizza", "Fries", "Coke"]
    prices = [5.99, 12.99, 2.99, 1.50]
    
    while True:
        display_app_menu(items, prices)
        
        print("\\n1. Add Item")
        print("2. Remove Item")
        print("3. Apply 10% Discount to All")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            new_item = input("Enter item name: ")
            try:
                new_price = float(input("Enter price: $"))
                items.append(new_item)
                prices.append(new_price)
                print("Added.")
            except ValueError:
                print("Invalid price.")
                
        elif choice == '2':
            item_to_remove = input("Enter exact item name to remove: ")
            if item_to_remove in items:
                idx = items.index(item_to_remove)
                items.pop(idx)
                prices.pop(idx)
                print(f"Removed {item_to_remove}.")
            else:
                print("Item not found.")
                
        elif choice == '3':
            # List comprehension to apply discount
            prices = [round(price * 0.90, 2) for price in prices]
            print("10% discount applied to all items!")
            
        elif choice == '4':
            break

if __name__ == "__main__":
    run_swiggy_manager()
