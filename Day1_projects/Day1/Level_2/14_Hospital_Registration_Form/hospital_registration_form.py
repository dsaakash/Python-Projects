
# ============================================
#  Project 14: Hospital Registration Form
#  Topics Used: print(), input()
# ============================================

print("=" * 55)
print("         HOSPITAL REGISTRATION FORM")
print("=" * 55)
print("  🏥 Welcome to City General Hospital 🏥")
print("=" * 55)

print("\n--- PATIENT INFORMATION ---")
patient_name = input("Enter patient full name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
age = input("Enter age: ")
gender = input("Enter gender (Male/Female/Other): ")
blood_group = input("Enter blood group (A+/B+/O+/AB+/etc): ")
address = input("Enter home address: ")
city = input("Enter city: ")
pincode = input("Enter pincode: ")
phone = input("Enter phone number: ")
email = input("Enter email ID (or 'NA'): ")

print("\n--- EMERGENCY CONTACT ---")
emergency_name = input("Enter emergency contact name: ")
relation = input("Enter relation to patient: ")
emergency_phone = input("Enter emergency contact phone: ")

print("\n--- MEDICAL INFORMATION ---")
doctor = input("Enter doctor's name (if known, else 'Not Decided'): ")
department = input("Enter department (General/Cardiology/Ortho/etc): ")
complaint = input("Enter main health complaint: ")
insurance = input("Do you have health insurance? (Yes/No): ")

# Generate Patient ID
import random
patient_id = "HOSP" + str(random.randint(10000, 99999))

print()
print("=" * 55)
print("        🏥 HOSPITAL ADMISSION SLIP 🏥")
print("=" * 55)
print(f"  Patient ID   : {patient_id}")
print(f"  Name         : {patient_name}")
print(f"  DOB / Age    : {dob} / {age} yrs")
print(f"  Gender       : {gender}")
print(f"  Blood Group  : {blood_group}")
print(f"  Address      : {address}, {city} - {pincode}")
print(f"  Phone        : {phone}")
print(f"  Email        : {email}")
print(f"  {'─' * 50}")
print(f"  Emergency    : {emergency_name} ({relation}) - {emergency_phone}")
print(f"  {'─' * 50}")
print(f"  Doctor       : {doctor}")
print(f"  Department   : {department}")
print(f"  Complaint    : {complaint}")
print(f"  Insurance    : {insurance}")
print("=" * 55)
print("  ✅ Patient Successfully Registered!")
print("  🙏 Wishing you a speedy recovery!")
print("=" * 55)
