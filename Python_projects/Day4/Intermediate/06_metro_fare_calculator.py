"""
Intermediate Project 6: Metro Fare Calculator
Demonstrates Comparison and Logical Operators.
Clean Code Principles: Constants for configuration, clean logic.
"""

def calculate_metro_fare(stations_traveled, is_peak_hour, is_senior_citizen):
    BASE_FARE = 10.0
    FARE_PER_STATION = 2.5
    PEAK_HOUR_MULTIPLIER = 1.2
    SENIOR_DISCOUNT_PERCENT = 0.50 # 50% discount
    
    if stations_traveled <= 0:
        return 0.0
        
    fare = BASE_FARE + (stations_traveled * FARE_PER_STATION)
    
    if is_peak_hour:
        fare *= PEAK_HOUR_MULTIPLIER
        
    if is_senior_citizen:
        fare -= (fare * SENIOR_DISCOUNT_PERCENT)
        
    return round(fare, 2)

def run_metro_calculator():
    print("--- Metro Fare Calculator ---")
    
    try:
        stations = int(input("Enter number of stations traveled: "))
        
        peak_input = input("Is it peak hours? (yes/no): ").lower()
        is_peak_hour = (peak_input == 'yes')
        
        senior_input = input("Are you a senior citizen? (yes/no): ").lower()
        is_senior_citizen = (senior_input == 'yes')
        
        total_fare = calculate_metro_fare(stations, is_peak_hour, is_senior_citizen)
        
        print(f"\\nTotal Fare: ${total_fare:.2f}")
        
    except ValueError:
        print("Invalid input for stations. Please enter a number.")

if __name__ == "__main__":
    run_metro_calculator()
