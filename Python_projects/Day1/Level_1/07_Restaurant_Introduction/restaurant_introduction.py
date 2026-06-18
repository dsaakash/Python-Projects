
# ============================================
#  Project 7: Restaurant Introduction
#  Topics Used: print(), input()
# ============================================

print("=" * 45)
print("      RESTAURANT INTRODUCTION")
print("=" * 45)

rest_name = input("Enter restaurant name: ")
location = input("Enter restaurant location: ")
cuisine = input("Enter type of cuisine: ")
owner = input("Enter owner's name: ")
timing = input("Enter opening timing (e.g. 10AM - 11PM): ")
specialty = input("Enter specialty dish: ")
price_range = input("Enter price range for 2 people (in Rs): ")
contact = input("Enter contact number: ")

print()
print("=" * 45)
print("      🍽️  RESTAURANT MENU CARD 🍽️")
print("=" * 45)
print(f"  🏷️  Name      : {rest_name}")
print(f"  📍 Location  : {location}")
print(f"  🍛 Cuisine   : {cuisine}")
print(f"  👨‍🍳 Owner     : {owner}")
print(f"  ⏰ Timing    : {timing}")
print(f"  ⭐ Specialty : {specialty}")
print(f"  💰 Price/2   : Rs. {price_range}")
print(f"  📞 Contact   : {contact}")
print("=" * 45)
print("   😋 Come Hungry, Leave Happy! 😋")
print("=" * 45)
