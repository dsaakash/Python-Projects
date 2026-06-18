"""
Intermediate Project 8: Hospital Bill Calculator
Demonstrates Arithmetic Operators.
Clean Code Principles: Meaningful function names, clear calculations.
"""

def calculate_hospital_bill(room_rate, days, doctor_fees, medicine_cost):
    total_room_cost = room_rate * days
    subtotal = total_room_cost + doctor_fees + medicine_cost
    
    TAX_RATE = 0.05 # 5% tax
    tax_amount = subtotal * TAX_RATE
    
    grand_total = subtotal + tax_amount
    return grand_total, subtotal, tax_amount

def run_hospital_calculator():
    print("--- Hospital Bill Calculator ---")
    
    try:
        room_rate = float(input("Enter daily room rent: $"))
        days_admitted = int(input("Enter number of days admitted: "))
        doctor_fees = float(input("Enter total doctor consultation fees: $"))
        medicine_cost = float(input("Enter total medicine cost: $"))
        
        grand_total, subtotal, tax = calculate_hospital_bill(room_rate, days_admitted, doctor_fees, medicine_cost)
        
        print("\\n--- Final Hospital Bill ---")
        print(f"Room Charges ({days_admitted} days): ${room_rate * days_admitted:.2f}")
        print(f"Doctor Fees: ${doctor_fees:.2f}")
        print(f"Medicine Cost: ${medicine_cost:.2f}")
        print("---------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (5%): ${tax:.2f}")
        print(f"Grand Total: ${grand_total:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    run_hospital_calculator()
