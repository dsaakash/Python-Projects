"""
Intermediate Project 9: Zomato Menu App
Concepts: List sorting by multiple criteria (using lambda functions with sorting).
"""

def display_menu(menu):
    print(f"\\n{'Item':<20} | {'Rating':<6} | {'Price':<6}")
    print("-" * 38)
    for item in menu:
        print(f"{item[0]:<20} | {item[1]:<6} | ${item[2]:<6.2f}")

def run_zomato_app():
    # [Item Name, User Rating (out of 5), Price]
    menu = [
        ["Pasta", 4.2, 12.0],
        ["Pizza", 4.8, 15.0],
        ["Salad", 3.9, 8.0],
        ["Burger", 4.5, 9.0],
        ["Steak", 4.8, 25.0]
    ]
    
    print("--- Zomato App Menu Sorting ---")
    
    while True:
        print("\\n1. View Default Menu")
        print("2. Sort by Price (Low to High)")
        print("3. Sort by Rating (High to Low)")
        print("4. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            display_menu(menu)
            
        elif choice == '2':
            # Sort using a lambda function pointing to index 2 (Price)
            sorted_by_price = sorted(menu, key=lambda x: x[2])
            display_menu(sorted_by_price)
            
        elif choice == '3':
            # Sort using lambda pointing to index 1 (Rating), reverse=True
            sorted_by_rating = sorted(menu, key=lambda x: x[1], reverse=True)
            display_menu(sorted_by_rating)
            
        elif choice == '4':
            break

if __name__ == "__main__":
    run_zomato_app()
