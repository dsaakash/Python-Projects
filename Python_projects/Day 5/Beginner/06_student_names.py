"""
Beginner Project 6: Student Names
Concepts: Iterating over lists, using count(), string methods with lists.
"""

def display_students(students):
    print("\\nList of Students:")
    for name in students:
        print(f"- {name.title()}")

def run_student_manager():
    students = ["alice", "bob", "charlie", "alice", "diana"]
    
    print("--- Class Attendance Tracker ---")
    display_students(students)
    
    # Using count()
    name_to_search = "alice"
    occurrences = students.count(name_to_search)
    print(f"\\nThe name '{name_to_search.title()}' appears {occurrences} time(s) in the list.")
    
    # Adding a new student
    new_student = input("\\nEnter a new student name to add: ").strip().lower()
    if new_student:
        students.append(new_student)
        print(f"Added {new_student.title()}.")
        
    display_students(students)

if __name__ == "__main__":
    run_student_manager()
