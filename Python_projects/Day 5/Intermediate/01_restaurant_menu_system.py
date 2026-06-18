"""
Intermediate Project 1: Restaurant Menu System
Concepts: List of lists (Nested Lists), formatting output.
"""

def display_menu(menu):
    print("\\n--- Restaurant Menu ---")
    print(f"{'ID':<5} | {'Item Name':<20} | {'Price':<10}")
    print("-" * 40)
    for index, item in enumerate(menu):
        # item is a nested list: [name, price]
        print(f"{index + 1:<5} | {item[0]:<20} | ${item[1]:<10.2f}")
    print("-" * 40)

def run_menu_system():
    # Nested list representing [Item Name, Price]
    menu = [
        ["Margherita Pizza", 12.99],
        ["Pasta Carbonara", 14.50],
        ["Caesar Salad", 8.99],
        ["Garlic Bread", 4.50]
    ]
    
    while True:
        display_menu(menu)
        print("1. Add new item")
        print("2. Remove item")
        print("3. Update price")
        print("4. Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: $"))
                menu.append([name, price])
                print("Item added successfully.")
            except ValueError:
                print("Invalid price.")
                
        elif choice == '2':
            try:
                item_id = int(input("Enter ID of item to remove: "))
                if 1 <= item_id <= len(menu):
                    removed_item = menu.pop(item_id - 1)
                    print(f"Removed {removed_item[0]}")
                else:
                    print("Invalid ID.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            try:
                item_id = int(input("Enter ID of item to update: "))
                if 1 <= item_id <= len(menu):
                    new_price = float(input("Enter new price: $"))
                    menu[item_id - 1][1] = new_price # Modifying nested list element
                    print("Price updated.")
                else:
                    print("Invalid ID.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_menu_system()
