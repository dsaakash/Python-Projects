
# ============================================
#  Project 8: My Family Details
#  Topics Used: print(), input()
# ============================================

print("=" * 45)
print("         MY FAMILY DETAILS")
print("=" * 45)

family_name = input("Enter your family/surname: ")
members = input("Enter total family members: ")

print("\n--- Father's Details ---")
father_name = input("Enter father's name: ")
father_job = input("Enter father's occupation: ")

print("\n--- Mother's Details ---")
mother_name = input("Enter mother's name: ")
mother_job = input("Enter mother's occupation: ")

print("\n--- About You ---")
my_name = input("Enter your name: ")
my_class = input("Enter your class/course: ")

hometown = input("\nEnter your hometown: ")

print()
print("=" * 45)
print("      👨‍👩‍👧‍👦 MY FAMILY CARD 👨‍👩‍👧‍👦")
print("=" * 45)
print(f"  🏠 Family Name  : {family_name}")
print(f"  👥 Members      : {members}")
print(f"  👨 Father       : {father_name} ({father_job})")
print(f"  👩 Mother       : {mother_name} ({mother_job})")
print(f"  🧑 Me           : {my_name} ({my_class})")
print(f"  🏡 Hometown     : {hometown}")
print("=" * 45)
print("   ❤️  Family is Everything! ❤️")
print("=" * 45)
