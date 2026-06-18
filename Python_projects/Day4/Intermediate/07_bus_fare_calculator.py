"""
Intermediate Project 7: Bus Fare Calculator
Demonstrates Arithmetic and Comparison Operators.
Clean Code Principles: Clean conditional branching, isolated calculation.
"""

def calculate_bus_fare(distance_km, passenger_type):
    BASE_FARE = 5.0
    RATE_PER_KM = 1.5
    
    fare = BASE_FARE + (distance_km * RATE_PER_KM)
    
    # Apply discounts based on passenger type
    if passenger_type == 'student':
        fare *= 0.75 # 25% discount
    elif passenger_type == 'child':
        fare *= 0.50 # 50% discount
        
    return round(fare, 2)

def run_bus_calculator():
    print("--- Bus Fare Calculator ---")
    
    try:
        distance = float(input("Enter travel distance in km: "))
        if distance <= 0:
            print("Distance must be positive.")
            return
            
        print("Passenger Types: standard, student, child")
        passenger_type = input("Enter passenger type: ").lower()
        
        if passenger_type not in ['standard', 'student', 'child']:
            print("Invalid passenger type. Defaulting to standard.")
            passenger_type = 'standard'
            
        fare = calculate_bus_fare(distance, passenger_type)
        print(f"\\nTicket Price for {passenger_type}: ${fare:.2f}")
        
    except ValueError:
        print("Invalid input for distance.")

if __name__ == "__main__":
    run_bus_calculator()
