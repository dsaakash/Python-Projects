"""
Beginner Project 7: Salary Calculator
Demonstrates Arithmetic and Comparison Operators.
Clean Code Principles: Magic numbers extracted to constants, single responsibility functions.
"""

def calculate_gross_salary(basic_salary):
    HRA_PERCENTAGE = 0.20 # House Rent Allowance (20% of basic)
    DA_PERCENTAGE = 0.50  # Dearness Allowance (50% of basic)
    
    hra = basic_salary * HRA_PERCENTAGE
    da = basic_salary * DA_PERCENTAGE
    
    return basic_salary + hra + da

def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions

def is_eligible_for_tax(net_salary):
    TAX_THRESHOLD = 50000
    return net_salary > TAX_THRESHOLD

def run_salary_calculator():
    print("--- Employee Salary Calculator ---")
    try:
        basic_salary = float(input("Enter employee basic salary: $"))
        pf_deduction = float(input("Enter Provident Fund (PF) deduction: $"))
        
        gross_salary = calculate_gross_salary(basic_salary)
        net_salary = calculate_net_salary(gross_salary, pf_deduction)
        
        print("\\n--- Salary Breakdown ---")
        print(f"Basic Salary: ${basic_salary:.2f}")
        print(f"Gross Salary: ${gross_salary:.2f}")
        print(f"Deductions (PF): ${pf_deduction:.2f}")
        print(f"Net Salary: ${net_salary:.2f}")
        
        # Logical / Comparison operators
        if is_eligible_for_tax(net_salary):
            print("Note: This salary falls into the taxable bracket.")
        else:
            print("Note: This salary is tax-free.")
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    run_salary_calculator()
