"""
Beginner Project 2: IPL Team List
Concepts: Pre-populated lists, slicing, insert().
"""

def run_ipl_manager():
    # Initializing a list with some data
    teams = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore"]
    
    print("--- IPL Team Roster Manager ---")
    print("Initial Teams:", teams)
    
    # Inserting a new team at a specific index
    print("\\nInserting 'Delhi Capitals' at index 1...")
    teams.insert(1, "Delhi Capitals")
    print("Current Teams:", teams)
    
    print("\\nInserting 'Kolkata Knight Riders' at the end using insert()...")
    teams.insert(len(teams), "Kolkata Knight Riders")
    print("Current Teams:", teams)
    
    # Slicing examples
    print("\\n--- List Slicing Examples ---")
    print(f"First two teams (teams[0:2]): {teams[0:2]}")
    print(f"Last two teams (teams[-2:]): {teams[-2:]}")
    print(f"Every second team (teams[::2]): {teams[::2]}")
    
    print("\\nFinal Team List:")
    for team in teams:
        print(f"- {team}")

if __name__ == "__main__":
    run_ipl_manager()
