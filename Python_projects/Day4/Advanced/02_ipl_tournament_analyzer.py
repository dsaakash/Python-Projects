"""
Advanced Project 2: IPL Tournament Analyzer
Demonstrates Assignment, Logical, and Arithmetic Operators.
Clean Code Principles: Separated scoring logic, readable loop execution.
"""

def calculate_points(wins, ties, no_results):
    POINTS_PER_WIN = 2
    POINTS_PER_TIE = 1
    POINTS_PER_NR = 1
    
    total_points = (wins * POINTS_PER_WIN) + (ties * POINTS_PER_TIE) + (no_results * POINTS_PER_NR)
    return total_points

def run_tournament_analyzer():
    print("--- IPL Tournament Analyzer ---")
    
    teams = {}
    num_teams = 3 # Limiting to 3 for demonstration
    
    print(f"Enter details for {num_teams} teams:")
    for i in range(num_teams):
        try:
            name = input(f"\\nTeam {i+1} Name: ")
            matches_played = int(input("Matches Played: "))
            wins = int(input("Wins: "))
            losses = int(input("Losses: "))
            ties = int(input("Ties: "))
            no_results = int(input("No Results: "))
            
            # Validation
            if (wins + losses + ties + no_results) != matches_played:
                print("Error: Match outcomes do not add up to total matches played.")
                continue
                
            points = calculate_points(wins, ties, no_results)
            teams[name] = {
                'played': matches_played,
                'wins': wins,
                'points': points
            }
        except ValueError:
            print("Invalid input. Skipping team.")

    print("\\n--- Tournament Points Table ---")
    print(f"{'Team':<15} {'Played':<8} {'Wins':<6} {'Points':<6}")
    
    # Using logical and comparison operators to find the top team
    top_team = None
    max_points = -1
    
    for team, stats in teams.items():
        print(f"{team:<15} {stats['played']:<8} {stats['wins']:<6} {stats['points']:<6}")
        
        if stats['points'] > max_points:
            max_points = stats['points']
            top_team = team
            
    if top_team:
        print(f"\\nCurrent Table Topper: {top_team} with {max_points} points!")

if __name__ == "__main__":
    run_tournament_analyzer()
