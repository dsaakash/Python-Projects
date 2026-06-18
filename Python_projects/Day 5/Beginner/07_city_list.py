"""
Beginner Project 7: City List
Concepts: list copying (shallow copy vs deep copy intro), clear().
"""

def run_city_list():
    cities = ["New York", "London", "Tokyo", "Paris"]
    print("--- Travel Itinerary ---")
    print("Original Cities:", cities)
    
    # Incorrect way to copy (reference only)
    cities_reference = cities
    
    # Correct way to create a shallow copy
    cities_copy = cities.copy()
    # OR: cities_copy = list(cities)
    # OR: cities_copy = cities[:]
    
    print("\\nAdding 'Sydney' to the ORIGINAL list...")
    cities.append("Sydney")
    
    print("\\nLet's check our lists:")
    print("Original Cities:", cities)
    print("Referenced List (changes too):", cities_reference)
    print("Copied List (remains unchanged):", cities_copy)
    
    print("\\nClearing the original list...")
    cities.clear()
    
    print("Original after clear:", cities)
    print("Copied list is safe:", cities_copy)

if __name__ == "__main__":
    run_city_list()
