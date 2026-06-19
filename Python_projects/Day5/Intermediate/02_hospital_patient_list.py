"""
Intermediate Project 2: Hospital Patient List
Concepts: Advanced slicing, reversing, filtering.
"""

def display_patients(patients):
    if not patients:
        print("No patients currently admitted.")
        return
    for i, p in enumerate(patients):
        print(f"[{i}] {p}")

def run_patient_list():
    # Using a flat list for simplicity, simulating queue
    patients = ["John Doe", "Jane Smith", "Bob Brown", "Alice White", "Charlie Green"]
    
    print("--- Emergency Room Queue ---")
    
    print("\\nCurrent Queue:")
    display_patients(patients)
    
    print("\\nNext 3 patients to be seen (slicing patients[:3]):")
    display_patients(patients[:3])
    
    print("\\nReversing the queue order (simulating LIFO instead of FIFO):")
    # slicing [::-1] creates a reversed copy
    reversed_patients = patients[::-1]
    display_patients(reversed_patients)
    
    print("\\nAdmitting new high-priority patient to the front of the line (index 0):")
    patients.insert(0, "EMERGENCY: Unknown Male")
    display_patients(patients)
    
    print("\\nDischarging patient 'Jane Smith':")
    if "Jane Smith" in patients:
        patients.remove("Jane Smith")
        print("Discharged.")
        
    print("\\nFinal Queue:")
    display_patients(patients)

if __name__ == "__main__":
    run_patient_list()
