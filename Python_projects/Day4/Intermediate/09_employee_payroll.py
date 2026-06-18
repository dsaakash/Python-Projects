"""
Intermediate Project 9: Employee Payroll System
Demonstrates Arithmetic and Logical Operators.
Clean Code Principles: Structured breakdown of complex calculations.
"""

def calculate_overtime_pay(hours_worked, hourly_rate):
    STANDARD_HOURS = 40
    OVERTIME_MULTIPLIER = 1.5
    
    if hours_worked > STANDARD_HOURS:
        overtime_hours = hours_worked - STANDARD_HOURS
        return overtime_hours * (hourly_rate * OVERTIME_MULTIPLIER)
    return 0.0

def calculate_regular_pay(hours_worked, hourly_rate):
    STANDARD_HOURS = 40
    regular_hours = min(hours_worked, STANDARD_HOURS)
    return regular_hours * hourly_rate

def run_payroll():
    print("--- Employee Payroll ---")
    
    try:
        hours_worked = float(input("Enter total hours worked this week: "))
        hourly_rate = float(input("Enter hourly wage rate: $"))
        
        if hours_worked < 0 or hourly_rate < 0:
            print("Values cannot be negative.")
            return
            
        regular_pay = calculate_regular_pay(hours_worked, hourly_rate)
        overtime_pay = calculate_overtime_pay(hours_worked, hourly_rate)
        total_pay = regular_pay + overtime_pay
        
        print("\\n--- Payroll Summary ---")
        print(f"Regular Pay: ${regular_pay:.2f}")
        if overtime_pay > 0:
            print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Total Gross Pay: ${total_pay:.2f}")
        
    except ValueError:
        print("Invalid numeric input.")

if __name__ == "__main__":
    run_payroll()
