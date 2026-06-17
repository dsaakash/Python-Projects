
# ============================================
#  Project 18: Gym Registration Form
#  Topics Used: print(), input()
# ============================================

print("=" * 50)
print("          GYM REGISTRATION FORM")
print("=" * 50)
print("  💪 Welcome to FitPython Gym & Fitness 💪")
print("=" * 50)

print("\n--- PERSONAL DETAILS ---")
name = input("Enter your full name: ")
age = input("Enter your age: ")
gender = input("Enter gender (Male/Female/Other): ")
phone = input("Enter phone number: ")
email = input("Enter email ID: ")
blood_group = input("Enter blood group: ")
medical_condition = input("Any medical condition? (Yes/No - if Yes, specify): ")

print("\n--- FITNESS DETAILS ---")
height = input("Enter height (in cm): ")
weight = input("Enter weight (in kg): ")
goal = input("Fitness goal (Weight Loss/Muscle Gain/Fitness/Sports): ")
experience = input("Gym experience (Beginner/Intermediate/Advanced): ")

print("\n--- MEMBERSHIP DETAILS ---")
plan = input("Choose plan (Monthly/Quarterly/Half-Yearly/Annual): ")
trainer = input("Do you need personal trainer? (Yes/No): ")
timing = input("Preferred timing (Morning/Evening/Night): ")
start_date = input("Enter start date (DD/MM/YYYY): ")

# Fee calculation
fees = {"monthly": 1500, "quarterly": 4000, "half-yearly": 7000, "annual": 12000}
trainer_fee = 2000 if trainer.lower() == "yes" else 0
base_fee = fees.get(plan.lower(), 1500)
total_fee = base_fee + trainer_fee

import random
member_id = "GYM" + str(random.randint(10000, 99999))

print()
print("=" * 50)
print("      💪 GYM MEMBERSHIP CARD 💪")
print("=" * 50)
print(f"  Member ID    : {member_id}")
print(f"  Name         : {name}")
print(f"  Age/Gender   : {age} / {gender}")
print(f"  Phone        : {phone}")
print(f"  Blood Group  : {blood_group}")
print(f"  Height       : {height} cm | Weight: {weight} kg")
print(f"  Fitness Goal : {goal}")
print(f"  Level        : {experience}")
print(f"  {'─' * 44}")
print(f"  Plan         : {plan.capitalize()}")
print(f"  Timing       : {timing}")
print(f"  Start Date   : {start_date}")
print(f"  Trainer      : {trainer}")
print(f"  {'─' * 44}")
print(f"  Membership   : Rs. {base_fee}")
print(f"  Trainer Fee  : Rs. {trainer_fee}")
print(f"  TOTAL FEES   : Rs. {total_fee}")
print("=" * 50)
print("  ✅ Welcome to FitPython Gym! Let's Get Fit! 💪")
print("=" * 50)
