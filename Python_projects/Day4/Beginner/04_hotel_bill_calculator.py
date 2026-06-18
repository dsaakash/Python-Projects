"""
Beginner Project 4: Hotel Bill Calculator
Demonstrates Arithmetic and Assignment Operators.
Clean Code Principles: Clear calculation flow, no magic numbers.
"""

def calculate_total_room_cost(room_rate, nights_stayed):
    return room_rate * nights_stayed

def calculate_total_food_cost(food_expenses):
    total = 0
    for expense in food_expenses:
        total += expense # Assignment operator
    return total

def calculate_grand_total(room_cost, food_cost, service_charge_rate):
    subtotal = room_cost + food_cost
    service_charge = subtotal * service_charge_rate
    grand_total = subtotal + service_charge
    return round(grand_total, 2)

def run_hotel_calculator():
    SERVICE_CHARGE_RATE = 0.05 # 5% service charge
    
    print("--- Hotel Bill Calculator ---")
    try:
        room_rate = float(input("Enter room rate per night: $"))
        nights_stayed = int(input("Enter number of nights stayed: "))
        
        food_expense_count = int(input("How many food orders were made? "))
        food_expenses = []
        for i in range(food_expense_count):
            cost = float(input(f"Enter cost of food order {i+1}: $"))
            food_expenses.append(cost)

        room_cost = calculate_total_room_cost(room_rate, nights_stayed)
        food_cost = calculate_total_food_cost(food_expenses)
        
        grand_total = calculate_grand_total(room_cost, food_cost, SERVICE_CHARGE_RATE)
        
        print("\\n--- Bill Summary ---")
        print(f"Room Charges: ${room_cost:.2f}")
        print(f"Food Charges: ${food_cost:.2f}")
        print(f"Service Charge ({SERVICE_CHARGE_RATE * 100}%): ${(room_cost + food_cost) * SERVICE_CHARGE_RATE:.2f}")
        print(f"Grand Total: ${grand_total:.2f}")
        print("--------------------")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    run_hotel_calculator()
