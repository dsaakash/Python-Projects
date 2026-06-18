"""
Intermediate Project 5: Bus Passenger List
Concepts: Enumerate, inserting at specific indices (seating), checking capacity.
"""

def display_seats(seats):
    print("\\n--- Bus Seating Chart ---")
    for idx, passenger in enumerate(seats):
        status = "Empty" if passenger is None else passenger
        print(f"Seat {idx + 1:02d}: {status}")

def run_bus_system():
    TOTAL_SEATS = 10
    # Initialize list with None representing empty seats
    seats = [None] * TOTAL_SEATS
    
    while True:
        display_seats(seats)
        available_seats = seats.count(None)
        print(f"\\nAvailable Seats: {available_seats}/{TOTAL_SEATS}")
        
        if available_seats == 0:
            print("Bus is FULL!")
            break
            
        print("1. Book a specific seat")
        print("2. Book next available seat")
        print("3. Cancel booking")
        print("4. Depart (Exit)")
        
        choice = input("Choice: ")
        
        if choice == '1':
            name = input("Enter passenger name: ")
            try:
                seat_num = int(input(f"Enter seat number (1-{TOTAL_SEATS}): "))
                idx = seat_num - 1
                if 0 <= idx < TOTAL_SEATS:
                    if seats[idx] is None:
                        seats[idx] = name
                        print(f"Seat {seat_num} booked for {name}.")
                    else:
                        print("Seat is already taken!")
                else:
                    print("Invalid seat number.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            name = input("Enter passenger name: ")
            # Find first empty seat
            try:
                first_empty_idx = seats.index(None)
                seats[first_empty_idx] = name
                print(f"Booked next available seat: Seat {first_empty_idx + 1}")
            except ValueError:
                print("No seats available.")
                
        elif choice == '3':
            try:
                seat_num = int(input(f"Enter seat number to cancel (1-{TOTAL_SEATS}): "))
                idx = seat_num - 1
                if 0 <= idx < TOTAL_SEATS:
                    if seats[idx] is not None:
                        print(f"Booking for {seats[idx]} cancelled.")
                        seats[idx] = None
                    else:
                        print("Seat is already empty.")
                else:
                    print("Invalid seat number.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '4':
            print("Bus is departing!")
            break

if __name__ == "__main__":
    run_bus_system()
