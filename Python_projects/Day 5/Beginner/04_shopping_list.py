"""
Beginner Project 4: Shopping List
Concepts: Checking items (in keyword), list length (len()), list clearing.
"""

def run_shopping_list():
    shopping_cart = []
    
    print("--- Dynamic Shopping Cart ---")
    
    while True:
        print(f"\\nItems in cart: {len(shopping_cart)}")
        print("1. Add item")
        print("2. Check if item is in cart")
        print("3. Clear cart")
        print("4. Checkout (Exit)")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            item = input("What would you like to buy? ").strip()
            shopping_cart.append(item)
            print(f"Added {item}.")
            
        elif choice == '2':
            item = input("Enter item to search for: ").strip()
            # Using 'in' operator for lists
            if item in shopping_cart:
                print(f"Yes, {item} is already in your cart.")
            else:
                print(f"No, {item} is not in your cart.")
                
        elif choice == '3':
            shopping_cart.clear()
            print("Cart has been cleared!")
            
        elif choice == '4':
            print("\\n--- Receipt ---")
            if not shopping_cart:
                print("Cart is empty.")
            else:
                for item in shopping_cart:
                    print(f"- {item}")
            print("Thank you for shopping!")
            break
            
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    run_shopping_list()
