"""
Beginner Project 8: Mobile Brands
Concepts: Finding min/max in lists, simple list comprehension.
"""

def run_mobile_brands():
    brands = ["Apple", "Samsung", "OnePlus", "Google", "Xiaomi"]
    
    print("--- Mobile Brands Directory ---")
    print("Current Brands:", brands)
    
    # min() and max() on strings use alphabetical order
    first_alpha_brand = min(brands)
    last_alpha_brand = max(brands)
    
    print(f"\\nFirst brand alphabetically: {first_alpha_brand}")
    print(f"Last brand alphabetically: {last_alpha_brand}")
    
    # Introduction to list comprehension (creating a new list based on an existing one)
    print("\\nCreating a new list with brands that contain the letter 'o':")
    # Syntax: [expression for item in list if condition]
    brands_with_o = [brand for brand in brands if 'o' in brand.lower()]
    
    print(brands_with_o)
    
    print("\\nCreating a list of lengths of brand names:")
    brand_lengths = [len(brand) for brand in brands]
    print(brand_lengths)

if __name__ == "__main__":
    run_mobile_brands()
