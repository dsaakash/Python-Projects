
# ============================================
#  Project 16: Metro Passenger Form
#  Topics Used: print(), input()
# ============================================

print("=" * 50)
print("         METRO PASSENGER FORM")
print("=" * 50)
print("  🚇 Welcome to Python City Metro Rail 🚇")
print("=" * 50)

print("\n--- PASSENGER DETAILS ---")
name = input("Enter passenger name: ")
age = input("Enter age: ")
gender = input("Enter gender (Male/Female/Other): ")
phone = input("Enter phone number: ")
id_proof = input("Enter ID proof type (Aadhar/PAN/Passport): ")
id_number = input("Enter ID number: ")

print("\n--- JOURNEY DETAILS ---")
source = input("Enter source station: ")
destination = input("Enter destination station: ")
journey_date = input("Enter journey date (DD/MM/YYYY): ")
journey_time = input("Enter preferred time (Morning/Afternoon/Evening): ")
passengers = input("Enter number of passengers: ")
card_type = input("Card type (Single Journey/Daily Pass/Monthly Pass): ")

# Simple fare calculation
fare_map = {"single journey": 30, "daily pass": 100, "monthly pass": 800}
fare_per = fare_map.get(card_type.lower(), 30)
total_fare = fare_per * int(passengers)

# Generate Ticket ID
import random
ticket_id = "METRO" + str(random.randint(10000, 99999))

print()
print("=" * 50)
print("        🚇 METRO TICKET RECEIPT 🚇")
print("=" * 50)
print(f"  Ticket ID    : {ticket_id}")
print(f"  Passenger    : {name} ({age} yrs / {gender})")
print(f"  ID Proof     : {id_proof} - {id_number}")
print(f"  Phone        : {phone}")
print(f"  {'─' * 44}")
print(f"  From         : {source}")
print(f"  To           : {destination}")
print(f"  Date         : {journey_date} ({journey_time})")
print(f"  Passengers   : {passengers}")
print(f"  Card Type    : {card_type}")
print(f"  {'─' * 44}")
print(f"  Fare/Person  : Rs. {fare_per}")
print(f"  TOTAL FARE   : Rs. {total_fare}")
print("=" * 50)
print("  ✅ Ticket Booked! Have a Safe Journey! 🚇")
print("=" * 50)
