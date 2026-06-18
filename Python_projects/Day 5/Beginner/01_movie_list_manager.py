"""
Beginner Project 1: Movie List Manager
Concepts: List creation, indexing, append(), remove().
"""

def display_movies(movies):
    print("\\n--- Current Movie Watchlist ---")
    if not movies:
        print("List is empty!")
    else:
        for index, movie in enumerate(movies):
            print(f"{index + 1}. {movie}")
    print("-------------------------------")

def run_movie_manager():
    watchlist = []
    
    while True:
        display_movies(watchlist)
        print("1. Add a movie")
        print("2. Remove a movie")
        print("3. View first and last movie")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            movie = input("Enter movie name: ").strip()
            watchlist.append(movie)
            print(f"'{movie}' added to watchlist.")
            
        elif choice == '2':
            movie = input("Enter movie name to remove: ").strip()
            if movie in watchlist:
                watchlist.remove(movie)
                print(f"'{movie}' removed.")
            else:
                print("Movie not found in the list.")
                
        elif choice == '3':
            if len(watchlist) > 0:
                print(f"First Movie: {watchlist[0]}") # Indexing
                print(f"Last Movie: {watchlist[-1]}") # Negative Indexing
            else:
                print("Not enough movies in the list.")
                
        elif choice == '4':
            print("Exiting Movie Manager.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_movie_manager()
