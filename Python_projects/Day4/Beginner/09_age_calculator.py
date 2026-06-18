"""
Beginner Project 9: Age Calculator
Demonstrates Arithmetic and Logical Operators.
Clean Code Principles: Modular date calculation, descriptive names.
"""
import datetime

def calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    """Calculates exact age based on given birth date and current date."""
    age_in_years = current_year - birth_year
    
    # Logical and comparison operators to adjust age if birthday hasn't occurred this year
    has_birthday_passed = (current_month > birth_month) or (current_month == birth_month and current_day >= birth_day)
    
    if not has_birthday_passed:
        age_in_years -= 1
        
    return age_in_years

def run_age_calculator():
    print("--- Age Calculator ---")
    
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    try:
        birth_year = int(input("Enter birth year (e.g., 1990): "))
        birth_month = int(input("Enter birth month (1-12): "))
        birth_day = int(input("Enter birth day (1-31): "))
        
        # Basic validation
        if not (1 <= birth_month <= 12) or not (1 <= birth_day <= 31):
            print("Invalid month or day entered.")
            return

        age = calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day)
        
        print(f"\\nYour exact age is: {age} years old.")
        
        # Logical operators for categories
        if age >= 18:
            print("Status: Adult")
        elif age >= 13 and age < 18:
            print("Status: Teenager")
        else:
            print("Status: Child")
            
    except ValueError:
        print("Invalid input! Please enter integer numbers.")

if __name__ == "__main__":
    run_age_calculator()
