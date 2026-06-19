"""
Beginner Project 10: College Subjects
Concepts: Creating lists from string splitting, joining lists into strings.
"""

def run_subjects():
    print("--- College Subject Parser ---")
    
    # Taking comma-separated input and splitting it into a list
    user_input = input("Enter your subjects separated by commas (e.g. Math,Physics,Chemistry): ")
    
    # split() creates a list from a string
    subjects_list = user_input.split(',')
    
    # Cleaning up whitespace using list comprehension
    clean_subjects = [subject.strip() for subject in subjects_list if subject.strip()]
    
    if not clean_subjects:
        print("No valid subjects entered.")
        return
        
    print(f"\\nYou have enrolled in {len(clean_subjects)} subjects:")
    for idx, subject in enumerate(clean_subjects):
        print(f"Subject {idx + 1}: {subject}")
        
    # Joining a list back into a single string
    print("\\nGenerating official transcript header...")
    transcript_header = " | ".join(clean_subjects)
    print(f"TRANSCRIPT: [ {transcript_header} ]")

if __name__ == "__main__":
    run_subjects()
