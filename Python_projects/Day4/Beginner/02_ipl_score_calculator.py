"""
Beginner Project 2: IPL Score Calculator
Demonstrates Assignment and Arithmetic Operators.
Clean Code Principles: Meaningful names, clear flow.
"""

def calculate_total_runs(singles, doubles, boundaries, sixes):
    """Calculates total score based on different types of scoring shots."""
    RUNS_PER_DOUBLE = 2
    RUNS_PER_BOUNDARY = 4
    RUNS_PER_SIX = 6

    total_runs = 0
    total_runs += singles
    total_runs += (doubles * RUNS_PER_DOUBLE)
    total_runs += (boundaries * RUNS_PER_BOUNDARY)
    total_runs += (sixes * RUNS_PER_SIX)
    
    return total_runs

def run_ipl_calculator():
    print("--- IPL Score Calculator ---")
    try:
        singles_scored = int(input("Enter number of singles (1s): "))
        doubles_scored = int(input("Enter number of doubles (2s): "))
        boundaries_scored = int(input("Enter number of boundaries (4s): "))
        sixes_scored = int(input("Enter number of sixes (6s): "))
        extras = int(input("Enter extras (wides/no-balls): "))

        batsman_runs = calculate_total_runs(singles_scored, doubles_scored, boundaries_scored, sixes_scored)
        
        # Assignment operator to add extras
        team_total = batsman_runs
        team_total += extras

        print("\\n--- Score Summary ---")
        print(f"Runs from bat: {batsman_runs}")
        print(f"Extras: {extras}")
        print(f"Total Team Score: {team_total}")

    except ValueError:
        print("Invalid input. Please enter valid integer numbers.")

if __name__ == "__main__":
    run_ipl_calculator()
