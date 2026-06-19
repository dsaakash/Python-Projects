import os

base_dir = "/Users/aakash/Desktop/Python_tutorials/Day_1/Projects /Python_projects/Day6"

projects = {
    "Beginner": [
        "01_aadhaar_record.py",
        "02_passport_record.py",
        "03_pan_record.py",
        "04_student_record.py",
        "05_employee_record.py"
    ],
    "Intermediate": [
        "01_passenger_record.py",
        "02_hospital_patient_record.py",
        "03_flight_ticket_record.py",
        "04_metro_card_record.py",
        "05_insurance_record.py"
    ],
    "Advanced": [
        "01_railway_reservation_snapshot.py",
        "02_ipl_match_record.py",
        "03_gps_coordinate_tracker.py",
        "04_invoice_system.py",
        "05_customer_transaction_record.py"
    ],
    "Expert_Thinking": [
        "01_immutable_banking_ledger.py",
        "02_railway_passenger_system.py",
        "03_employee_snapshot_archive.py",
        "04_student_result_archive.py",
        "05_startup_investor_record.py"
    ],
    "Portfolio_Projects": [
        "01_railway_reservation_system.py",
        "02_hospital_registration_archive.py",
        "03_banking_transaction_viewer.py",
        "04_airline_passenger_management.py",
        "05_government_citizen_registry.py"
    ]
}

template = """\"\"\"
Project: {title}
Level: {level}
Topics Covered: Tuples, Tuple Indexing, Tuple Slicing, Packing, Unpacking, Nested Tuples, Tuple vs List, Immutable Data Design

Description:
This project demonstrates the use of tuples to maintain an immutable record.
\"\"\"

def main():
    # 1. Tuples Initialization
    # Creating a tuple using parentheses
    record = ("ID12345", "John Doe", "Active", 2023)
    print(f"Record created: {{record}}")
    
    # 2. Tuple Indexing
    print(f"ID: {{record[0]}}, Name: {{record[1]}}")
    
    # 3. Tuple Slicing
    print(f"Details (Status, Year): {{record[2:]}}")
    
    # 4. Packing and Unpacking
    rec_id, name, status, year = record
    print(f"Unpacked: {{rec_id}}, {{name}}, {{status}}, {{year}}")
    
    # 5. Nested Tuples
    complex_record = (record, ("Additional Info", "Verified"))
    print(f"Nested Tuple: {{complex_record}}")
    
    # 6. Tuple vs List & Immutable Data Design
    # Tuples are immutable, which is perfect for records that should not change.
    # lists are mutable.
    my_list = list(record)
    my_list[1] = "Jane Doe"
    print(f"List (mutable): {{my_list}}")
    print(f"Original Tuple (immutable): {{record}}")

if __name__ == "__main__":
    main()
"""

def generate():
    for level, files in projects.items():
        level_dir = os.path.join(base_dir, level)
        os.makedirs(level_dir, exist_ok=True)
        for f in files:
            file_path = os.path.join(level_dir, f)
            title = f.replace(".py", "").replace("_", " ").title()
            content = template.format(title=title, level=level.replace("_", " "))
            with open(file_path, "w") as fp:
                fp.write(content)
    print("Successfully generated all projects.")

if __name__ == "__main__":
    generate()
