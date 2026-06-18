"""
Intermediate Project 10: Cricket Team Manager
Concepts: Handling multiple lists, moving elements between lists via pop and append.
"""

def display_squads(playing_xi, bench):
    print("\\n--- Playing XI ---")
    for p in playing_xi: print(f"- {p}")
    print("\\n--- Bench (Substitutes) ---")
    for p in bench: print(f"- {p}")

def run_team_manager():
    playing_xi = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]
    bench = ["Sub 1", "Sub 2", "Sub 3"]
    
    print("--- Team Selection Manager ---")
    
    while True:
        display_squads(playing_xi, bench)
        print("\\n1. Substitute Player")
        print("2. Add new player to bench")
        print("3. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            out_player = input("Who is coming OFF the field? (Playing XI): ")
            in_player = input("Who is going ON the field? (Bench): ")
            
            if out_player in playing_xi and in_player in bench:
                # Remove from playing, add to bench
                playing_xi.remove(out_player)
                bench.append(out_player)
                
                # Remove from bench, add to playing
                bench.remove(in_player)
                playing_xi.append(in_player)
                print("Substitution complete!")
            else:
                print("Invalid players entered.")
                
        elif choice == '2':
            new_player = input("Enter new player name: ")
            bench.append(new_player)
            print("Added to bench.")
            
        elif choice == '3':
            break

if __name__ == "__main__":
    run_team_manager()
