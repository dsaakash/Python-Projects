"""
Advanced Project 5: Amazon Cart System
Concepts: Nested lists, calculating totals, removing items by ID.
"""

def display_cart(cart):
    print(f"\\n{'Item ID':<8} | {'Product Name':<20} | {'Qty':<5} | {'Price/Unit':<10} | {'Subtotal':<10}")
    print("-" * 65)
    
    total_cost = 0.0
    for item in cart:
        subtotal = item[2] * item[3]
        total_cost += subtotal
        print(f"{item[0]:<8} | {item[1]:<20} | {item[2]:<5} | ${item[3]:<9.2f} | ${subtotal:<9.2f}")
        
    print("-" * 65)
    print(f"Total Cart Value: ${total_cost:.2f}")

def run_amazon_cart():
    # [Item ID, Name, Quantity, Price]
    cart = []
    item_counter = 100
    
    print("--- E-Commerce Shopping Cart ---")
    
    while True:
        print("\\n1. View Cart")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. Empty Cart")
        print("5. Checkout (Exit)")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            if not cart:
                print("Your cart is empty.")
            else:
                display_cart(cart)
                
        elif choice == '2':
            name = input("Enter product name: ")
            try:
                qty = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: $"))
                
                cart.append([item_counter, name, qty, price])
                print(f"Added '{name}' (ID: {item_counter}) to cart.")
                item_counter += 1
            except ValueError:
                print("Invalid number entered.")
                
        elif choice == '3':
            if not cart:
                print("Cart is already empty.")
                continue
                
            display_cart(cart)
            try:
                item_id = int(input("Enter Item ID to remove: "))
                
                # Finding the index of the item with the given ID
                index_to_remove = -1
                for idx, item in enumerate(cart):
                    if item[0] == item_id:
                        index_to_remove = idx
                        break
                        
                if index_to_remove != -1:
                    removed = cart.pop(index_to_remove)
                    print(f"Removed '{removed[1]}' from cart.")
                else:
                    print("Item ID not found in cart.")
            except ValueError:
                print("Invalid ID.")
                
        elif choice == '4':
            cart.clear()
            print("Cart emptied.")
            
        elif choice == '5':
            if cart:
                print("\\nProcessing final bill...")
                display_cart(cart)
                print("Thank you for your purchase!")
            else:
                print("Exiting without purchase.")
            break

if __name__ == "__main__":
    run_amazon_cart()
