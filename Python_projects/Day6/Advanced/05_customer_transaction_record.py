"""
Project: 05 Customer Transaction Record
Level: Advanced
Topics Covered: Tuples, Tuple Indexing, Tuple Slicing, Packing, Unpacking, Nested Tuples, Tuple vs List, Immutable Data Design

Description:
This project demonstrates the use of tuples to maintain an immutable record.
"""

def main():
    # 1. Tuples Initialization
    # Creating a tuple using parentheses
    record = ("ID12345", "John Doe", "Active", 2023)
    print(f"Record created: {record}")
    
    # 2. Tuple Indexing
    print(f"ID: {record[0]}, Name: {record[1]}")
    
    # 3. Tuple Slicing
    print(f"Details (Status, Year): {record[2:]}")
    
    # 4. Packing and Unpacking
    rec_id, name, status, year = record
    print(f"Unpacked: {rec_id}, {name}, {status}, {year}")
    
    # 5. Nested Tuples
    complex_record = (record, ("Additional Info", "Verified"))
    print(f"Nested Tuple: {complex_record}")
    
    # 6. Tuple vs List & Immutable Data Design
    # Tuples are immutable, which is perfect for records that should not change.
    # lists are mutable.
    my_list = list(record)
    my_list[1] = "Jane Doe"
    print(f"List (mutable): {my_list}")
    print(f"Original Tuple (immutable): {record}")

if __name__ == "__main__":
    main()
