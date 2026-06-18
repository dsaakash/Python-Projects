"""
Beginner Project 3: Cricket Average
Demonstrates Arithmetic and Comparison Operators.
Clean Code Principles: Small functions, meaningful names.
"""

def calculate_batting_average(total_runs, innings_played, not_outs):
    """Calculates batting average preventing division by zero."""
    dismissals = innings_played - not_outs
    
    if dismissals <= 0:
        return total_runs # Infinite/undefined average technically, but returning total runs is standard fallback
    
    average = total_runs / dismissals
    return round(average, 2)

def is_elite_batsman(average):
    """Determines if a batsman is elite based on average (> 50)."""
    ELITE_AVERAGE_THRESHOLD = 50.0
    return average >= ELITE_AVERAGE_THRESHOLD

def run_average_calculator():
    print("--- Cricket Average Calculator ---")
    try:
        player_name = input("Enter player name: ")
        total_runs = int(input(f"Enter total runs scored by {player_name}: "))
        innings_played = int(input("Enter total innings played: "))
        not_outs = int(input("Enter total not outs: "))

        if not_outs > innings_played:
            print("Error: Not outs cannot be greater than innings played.")
            return

        average = calculate_batting_average(total_runs, innings_played, not_outs)
        
        print(f"\\n{player_name}'s Batting Average: {average}")

        if is_elite_batsman(average):
            print(f"{player_name} has an Elite batting average!")
        else:
            print(f"{player_name} has a decent batting average.")

    except ValueError:
        print("Invalid input. Please enter numbers for runs and innings.")

if __name__ == "__main__":
    run_average_calculator()
