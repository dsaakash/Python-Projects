"""
Intermediate Project 10: Student Percentage Calculator
Demonstrates Arithmetic, Assignment, Comparison, and Logical Operators.
Clean Code Principles: Small functions, clean loops.
"""

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def run_percentage_calculator():
    print("--- Student Percentage & Grade Calculator ---")
    
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be at least 1.")
            return
            
        max_marks_per_subject = 100
        total_max_marks = num_subjects * max_marks_per_subject
        total_marks_obtained = 0
        
        for i in range(num_subjects):
            marks = float(input(f"Enter marks obtained for subject {i+1} (out of 100): "))
            
            if marks < 0 or marks > max_marks_per_subject:
                print(f"Invalid marks. Must be between 0 and {max_marks_per_subject}.")
                return
                
            total_marks_obtained += marks # Assignment Operator
            
        percentage = (total_marks_obtained / total_max_marks) * 100
        grade = calculate_grade(percentage)
        
        print("\\n--- Result ---")
        print(f"Total Marks: {total_marks_obtained}/{total_max_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    run_percentage_calculator()
