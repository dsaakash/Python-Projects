"""
Advanced Project 4: Student Management System
Concepts: Complex nested lists representing records, data aggregation (average).
"""

def display_students(students):
    print(f"\\n{'Roll':<5} | {'Name':<15} | {'Math':<5} | {'Sci':<5} | {'Eng':<5} | {'Avg %':<6}")
    print("-" * 55)
    for s in students:
        marks = s[2]
        avg = sum(marks) / len(marks)
        print(f"{s[0]:<5} | {s[1]:<15} | {marks[0]:<5} | {marks[1]:<5} | {marks[2]:<5} | {avg:<6.2f}%")

def run_student_system():
    # [Roll Number, Name, [Math, Science, English]]
    students = [
        [1, "Alice Smith", [85, 92, 88]],
        [2, "Bob Jones", [78, 81, 79]],
        [3, "Charlie Davis", [95, 98, 91]]
    ]
    
    print("--- School Management System ---")
    
    while True:
        print("\\n1. View All Students")
        print("2. Add New Student")
        print("3. Find Class Topper")
        print("4. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            display_students(students)
            
        elif choice == '2':
            try:
                roll = int(input("Enter Roll Number: "))
                if any(s[0] == roll for s in students):
                    print("Roll number already exists.")
                    continue
                    
                name = input("Enter Name: ")
                math = float(input("Enter Math marks: "))
                sci = float(input("Enter Science marks: "))
                eng = float(input("Enter English marks: "))
                
                students.append([roll, name, [math, sci, eng]])
                print("Student recorded.")
            except ValueError:
                print("Invalid numeric input.")
                
        elif choice == '3':
            if not students:
                print("No students in system.")
                continue
                
            # Find student with highest average
            topper = None
            highest_avg = -1
            
            for s in students:
                avg = sum(s[2]) / len(s[2])
                if avg > highest_avg:
                    highest_avg = avg
                    topper = s
                    
            print(f"\\nClass Topper: {topper[1]} with an average of {highest_avg:.2f}%")
            
        elif choice == '4':
            break

if __name__ == "__main__":
    run_student_system()
