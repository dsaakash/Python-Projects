
# ============================================
#  Project 15: Bank Account Opening Form
#  Topics Used: print(), input()
# ============================================

print("=" * 55)
print("       BANK ACCOUNT OPENING FORM")
print("=" * 55)
print("  🏦 Welcome to Python National Bank 🏦")
print("=" * 55)

print("\n--- PERSONAL DETAILS ---")
full_name = input("Enter your full name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
gender = input("Enter gender (Male/Female/Other): ")
pan = input("Enter PAN card number: ")
aadhar = input("Enter Aadhar card number (last 4 digits): ")
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

print("\n--- ADDRESS DETAILS ---")
address = input("Enter residential address: ")
city = input("Enter city: ")
state = input("Enter state: ")
pincode = input("Enter pincode: ")

print("\n--- ACCOUNT DETAILS ---")
account_type = input("Account type (Savings/Current/Salary): ")
initial_deposit = input("Enter initial deposit amount (Rs): ")
nominee_name = input("Enter nominee's full name: ")
nominee_relation = input("Enter nominee's relation: ")

# Generate Account Number
import random
acc_number = "PNB" + str(random.randint(100000000, 999999999))
ifsc = "PNB0001234"

print()
print("=" * 55)
print("     🏦 ACCOUNT OPENING CONFIRMATION 🏦")
print("=" * 55)
print(f"  Account No   : {acc_number}")
print(f"  IFSC Code    : {ifsc}")
print(f"  Account Type : {account_type}")
print(f"  {'─' * 50}")
print(f"  Name         : {full_name}")
print(f"  DOB          : {dob} | Gender: {gender}")
print(f"  PAN          : {pan}")
print(f"  Aadhar       : XXXX-XXXX-{aadhar}")
print(f"  Phone        : {phone}")
print(f"  Email        : {email}")
print(f"  Address      : {address}, {city}, {state} - {pincode}")
print(f"  {'─' * 50}")
print(f"  Initial Dep  : Rs. {initial_deposit}")
print(f"  Nominee      : {nominee_name} ({nominee_relation})")
print("=" * 55)
print("  ✅ Your bank account has been opened!")
print("  💳 Your debit card will arrive in 7 working days.")
print("=" * 55)
