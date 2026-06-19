"""
Advanced Project 2: Inventory Management
Concepts: Complex list of lists, list comprehension for stock alerts.
"""

def display_inventory(inventory):
    print(f"\\n{'SKU':<6} | {'Product':<20} | {'Stock':<6} | {'Price':<6}")
    print("-" * 45)
    for item in inventory:
        print(f"{item[0]:<6} | {item[1]:<20} | {item[2]:<6} | ${item[3]:<6.2f}")

def run_inventory_system():
    # [SKU, Name, Stock, Price]
    inventory = [
        [101, "Laptop", 5, 999.99],
        [102, "Mouse", 50, 19.99],
        [103, "Keyboard", 20, 49.99],
        [104, "Monitor", 2, 199.99]
    ]
    
    while True:
        display_inventory(inventory)
        print("\\n1. Update Stock")
        print("2. Add New Product")
        print("3. View Low Stock Alerts (< 10 units)")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                sku = int(input("Enter SKU to update: "))
                # Finding the item
                for item in inventory:
                    if item[0] == sku:
                        new_stock = int(input(f"Enter new stock quantity for {item[1]}: "))
                        item[2] = max(0, new_stock) # Prevent negative stock
                        print("Stock updated.")
                        break
                else:
                    print("SKU not found.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            try:
                sku = int(input("Enter new SKU: "))
                if any(item[0] == sku for item in inventory):
                    print("SKU already exists.")
                    continue
                    
                name = input("Enter Product Name: ")
                stock = int(input("Enter Initial Stock: "))
                price = float(input("Enter Price: $"))
                
                inventory.append([sku, name, stock, price])
                print("Product added.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            # Advanced list comprehension for filtering
            low_stock = [item for item in inventory if item[2] < 10]
            
            print("\\n--- LOW STOCK ALERTS ---")
            if not low_stock:
                print("All products have sufficient stock.")
            else:
                for item in low_stock:
                    print(f"URGENT: {item[1]} only has {item[2]} units left!")
                    
        elif choice == '4':
            break

if __name__ == "__main__":
    run_inventory_system()
