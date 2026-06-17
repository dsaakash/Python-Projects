
# ============================================
#  Project 17: Bus Reservation Form
#  Topics Used: print(), input()
# ============================================

print("=" * 55)
print("           BUS RESERVATION FORM")
print("=" * 55)
print("  🚌 Welcome to Python State Road Transport 🚌")
print("=" * 55)

print("\n--- PASSENGER DETAILS ---")
name = input("Enter passenger full name: ")
age = input("Enter age: ")
gender = input("Enter gender (Male/Female/Other): ")
phone = input("Enter phone number: ")

print("\n--- JOURNEY DETAILS ---")
source = input("Enter departure city: ")
destination = input("Enter destination city: ")
travel_date = input("Enter travel date (DD/MM/YYYY): ")
bus_type = input("Bus type (Sleeper/Seater/AC/Non-AC): ")
departure_time = input("Enter preferred departure time: ")
seats = input("Enter number of seats: ")
seat_pref = input("Seat preference (Window/Aisle/No Preference): ")

# Fare calculation
fare_map = {
    "sleeper": 600, "seater": 350,
    "ac": 800, "non-ac": 300
}
base_fare = fare_map.get(bus_type.lower(), 400)
total_fare = base_fare * int(seats)

import random
pnr = "PNR" + str(random.randint(1000000, 9999999))
seat_no = random.randint(1, 50)

print()
print("=" * 55)
print("        🚌 BUS TICKET RESERVATION 🚌")
print("=" * 55)
print(f"  PNR Number    : {pnr}")
print(f"  Passenger     : {name} | Age: {age} | {gender}")
print(f"  Phone         : {phone}")
print(f"  {'─' * 50}")
print(f"  From          : {source}")
print(f"  To            : {destination}")
print(f"  Travel Date   : {travel_date}")
print(f"  Departure     : {departure_time}")
print(f"  Bus Type      : {bus_type}")
print(f"  Seats Booked  : {seats}")
print(f"  Seat Number   : {seat_no} - {seat_pref}")
print(f"  {'─' * 50}")
print(f"  Fare/Seat     : Rs. {base_fare}")
print(f"  TOTAL AMOUNT  : Rs. {total_fare}")
print("=" * 55)
print("  ✅ Reservation Confirmed! Bon Voyage! 🚌")
print("=" * 55)
