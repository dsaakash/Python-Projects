"""
Beginner Project 6: Mobile EMI Calculator
Demonstrates Arithmetic Operators (exponentiation for formula).
Clean Code Principles: Formulas extracted to functions, meaningful names.
"""

def calculate_emi(principal, annual_interest_rate, tenure_months):
    """
    Calculates EMI using the formula: E = P * r * (1+r)^n / ((1+r)^n - 1)
    where r is the monthly interest rate.
    """
    if annual_interest_rate == 0:
        return principal / tenure_months

    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    numerator = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure_months)
    denominator = ((1 + monthly_interest_rate) ** tenure_months) - 1
    
    emi = numerator / denominator
    return round(emi, 2)

def run_emi_calculator():
    print("--- Mobile EMI Calculator ---")
    
    try:
        mobile_price = float(input("Enter mobile price: $"))
        down_payment = float(input("Enter down payment: $"))
        
        loan_principal = mobile_price - down_payment
        if loan_principal <= 0:
            print("No loan required! Down payment covers the cost.")
            return

        annual_rate = float(input("Enter annual interest rate (%): "))
        tenure_months = int(input("Enter EMI tenure in months: "))

        monthly_emi = calculate_emi(loan_principal, annual_rate, tenure_months)
        total_payment = down_payment + (monthly_emi * tenure_months)
        
        print("\\n--- EMI Details ---")
        print(f"Loan Amount: ${loan_principal:.2f}")
        print(f"Monthly EMI: ${monthly_emi:.2f}")
        print(f"Total Amount Paid (including Interest): ${total_payment:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    run_emi_calculator()
