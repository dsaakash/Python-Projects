"""
Beginner Project 3: Grocery List
Concepts: list combinations, remove(), pop(), index().
"""

def run_grocery_list():
    pantry_items = ["Rice", "Dal", "Salt"]
    fresh_items = ["Milk", "Eggs", "Bread", "Apples"]
    
    print("--- Grocery List App ---")
    
    # Combining lists
    grocery_list = pantry_items + fresh_items
    print("Full Grocery List:", grocery_list)
    
    # Finding index
    item_to_find = "Eggs"
    if item_to_find in grocery_list:
        index = grocery_list.index(item_to_find)
        print(f"\\n'{item_to_find}' is at position {index} (Index {index}).")
        
    # Removing items
    print("\\nRemoving 'Salt' using remove()...")
    grocery_list.remove("Salt")
    print("List:", grocery_list)
    
    print("\\nRemoving the last item using pop()...")
    removed_item = grocery_list.pop()
    print(f"Removed: {removed_item}")
    print("List:", grocery_list)
    
    print("\\nRemoving item at index 1 using pop(1)...")
    removed_item2 = grocery_list.pop(1)
    print(f"Removed: {removed_item2}")
    print("Final List:", grocery_list)

if __name__ == "__main__":
    run_grocery_list()
