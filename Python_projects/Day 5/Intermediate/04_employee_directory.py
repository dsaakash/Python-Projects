"""
Intermediate Project 4: Employee Directory
Concepts: List of Lists, data manipulation, updating.
"""

def display_employees(directory):
    print(f"\\n{'ID':<5} | {'Name':<15} | {'Department':<15}")
    print("-" * 40)
    for emp in directory:
        print(f"{emp[0]:<5} | {emp[1]:<15} | {emp[2]:<15}")

def run_directory():
    # [ID, Name, Department]
    directory = [
        [101, "John Smith", "HR"],
        [102, "Sarah Connor", "IT"],
        [103, "Bruce Wayne", "Management"]
    ]
    
    print("--- Company Directory ---")
    
    while True:
        display_employees(directory)
        print("\\n1. Add Employee")
        print("2. Search Employee by ID")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                emp_id = int(input("Enter new ID: "))
                # Check if ID exists
                if any(emp[0] == emp_id for emp in directory):
                    print("Error: ID already exists.")
                    continue
                    
                name = input("Enter Name: ")
                dept = input("Enter Department: ")
                
                directory.append([emp_id, name, dept])
                print("Employee added.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            try:
                search_id = int(input("Enter ID to search: "))
                found = False
                for emp in directory:
                    if emp[0] == search_id:
                        print(f"\\nFound: {emp[1]} from {emp[2]} Department.")
                        found = True
                        break
                if not found:
                    print("Employee not found.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            break

if __name__ == "__main__":
    run_directory()
