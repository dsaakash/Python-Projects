"""
Beginner Project 9: Programming Languages
Concepts: extend(), replacing elements by index.
"""

def run_languages():
    frontend = ["HTML", "CSS", "JavaScript"]
    backend = ["Python", "Java", "C++"]
    
    print("--- Full Stack Skills ---")
    print("Frontend:", frontend)
    print("Backend:", backend)
    
    # Using extend() to add multiple elements from another list
    print("\\nMerging backend into frontend using extend()...")
    # Note: frontend.append(backend) would create a nested list!
    frontend.extend(backend)
    
    full_stack = frontend 
    print("Full Stack List:", full_stack)
    
    print("\\nOops, let's replace 'C++' with 'Go'.")
    # Finding index and replacing
    if "C++" in full_stack:
        index_to_replace = full_stack.index("C++")
        full_stack[index_to_replace] = "Go" # Replacing via indexing
        
    print("Updated List:", full_stack)

if __name__ == "__main__":
    run_languages()
