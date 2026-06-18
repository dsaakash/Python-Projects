
# ============================================
#  Project 20: Customer Information Form
#  Topics Used: print(), input()
# ============================================

print("=" * 55)
print("         CUSTOMER INFORMATION FORM")
print("=" * 55)
print("  🛍️  Welcome to Python ShopEasy - Customer Portal 🛍️")
print("=" * 55)

print("\n--- PERSONAL DETAILS ---")
name = input("Enter customer full name: ")
age = input("Enter age: ")
gender = input("Enter gender (Male/Female/Other): ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
phone = input("Enter mobile number: ")
alt_phone = input("Enter alternate mobile number (or 'NA'): ")
email = input("Enter email ID: ")

print("\n--- ADDRESS DETAILS ---")
house = input("Enter house/flat number & street: ")
locality = input("Enter locality/area: ")
city = input("Enter city: ")
state = input("Enter state: ")
pincode = input("Enter pincode: ")

print("\n--- SHOPPING PREFERENCES ---")
category = input("Favourite shopping category (Electronics/Fashion/Grocery/etc): ")
payment = input("Preferred payment method (UPI/Card/COD/NetBanking): ")
membership = input("Choose membership (Basic/Silver/Gold/Platinum): ")

# Discount based on membership
discount_map = {"basic": 5, "silver": 10, "gold": 15, "platinum": 20}
discount = discount_map.get(membership.lower(), 5)

import random
customer_id = "CUST" + str(random.randint(100000, 999999))

print()
print("=" * 55)
print("        🛍️  CUSTOMER PROFILE CARD 🛍️")
print("=" * 55)
print(f"  Customer ID   : {customer_id}")
print(f"  Name          : {name}")
print(f"  Age/Gender    : {age} / {gender}")
print(f"  DOB           : {dob}")
print(f"  Mobile        : {phone}")
print(f"  Alt Mobile    : {alt_phone}")
print(f"  Email         : {email}")
print(f"  {'─' * 50}")
print(f"  Address       : {house}, {locality}")
print(f"                  {city}, {state} - {pincode}")
print(f"  {'─' * 50}")
print(f"  Category Pref : {category}")
print(f"  Payment Pref  : {payment}")
print(f"  Membership    : {membership.capitalize()}")
print(f"  Your Discount : {discount}% OFF on every order!")
print("=" * 55)
print("  ✅ Profile Created! Happy Shopping! 🛒")
print("=" * 55)
