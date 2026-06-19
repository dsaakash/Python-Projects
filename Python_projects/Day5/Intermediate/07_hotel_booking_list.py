"""
Intermediate Project 7: Hotel Booking List
Concepts: Matrix (List of lists), handling 2D data structures.
"""

def display_hotel_grid(hotel):
    print("\\n--- Hotel Floor Plan ---")
    for floor_idx, floor in enumerate(hotel):
        floor_num = len(hotel) - floor_idx
        print(f"Floor {floor_num}: ", end="")
        for room in floor:
            # 0 is empty, 1 is booked
            status = "[ X ]" if room == 1 else "[   ]"
            print(status, end=" ")
        print() # New line after floor

def run_hotel_booking():
    # 3 Floors, 4 Rooms per floor (0 = empty, 1 = booked)
    # Visualized top-down (Floor 3 is index 0)
    hotel = [
        [0, 1, 0, 0], # Floor 3
        [1, 1, 1, 0], # Floor 2
        [0, 0, 0, 0]  # Floor 1
    ]
    
    while True:
        display_hotel_grid(hotel)
        print("\\n1. Book a Room")
        print("2. Cancel Booking")
        print("3. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            try:
                floor = int(input("Enter floor (1-3): "))
                room = int(input("Enter room (1-4): "))
                
                # Convert human inputs to matrix indices
                f_idx = 3 - floor 
                r_idx = room - 1
                
                if 0 <= f_idx < 3 and 0 <= r_idx < 4:
                    if hotel[f_idx][r_idx] == 0:
                        hotel[f_idx][r_idx] = 1
                        print("Room booked successfully!")
                    else:
                        print("Room is already occupied.")
                else:
                    print("Invalid floor or room.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
             try:
                floor = int(input("Enter floor (1-3): "))
                room = int(input("Enter room (1-4): "))
                
                f_idx = 3 - floor 
                r_idx = room - 1
                
                if 0 <= f_idx < 3 and 0 <= r_idx < 4:
                    if hotel[f_idx][r_idx] == 1:
                        hotel[f_idx][r_idx] = 0
                        print("Booking cancelled.")
                    else:
                        print("Room is already empty.")
                else:
                    print("Invalid floor or room.")
             except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            break

if __name__ == "__main__":
    run_hotel_booking()
