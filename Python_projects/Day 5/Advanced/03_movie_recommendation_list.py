"""
Advanced Project 3: Movie Recommendation List
Concepts: Nested lists, filtering based on multiple tags (genres), list intersection.
"""

def display_movies(movies):
    print(f"\\n{'Title':<25} | {'Genres'}")
    print("-" * 50)
    for movie in movies:
        genres_str = ", ".join(movie[1])
        print(f"{movie[0]:<25} | {genres_str}")

def run_movie_recommender():
    # [Title, [List of Genres]]
    movies = [
        ["Inception", ["Sci-Fi", "Action", "Thriller"]],
        ["The Dark Knight", ["Action", "Crime", "Drama"]],
        ["Interstellar", ["Sci-Fi", "Drama", "Adventure"]],
        ["The Matrix", ["Sci-Fi", "Action"]],
        ["Toy Story", ["Animation", "Comedy", "Family"]]
    ]
    
    print("--- AI Movie Recommender ---")
    
    while True:
        print("\\n1. View All Movies")
        print("2. Get Recommendations by Genre")
        print("3. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            display_movies(movies)
            
        elif choice == '2':
            print("Available genres: Sci-Fi, Action, Thriller, Crime, Drama, Adventure, Animation, Comedy, Family")
            pref = input("Enter a genre you like: ").strip().title()
            
            # List comprehension to filter movies that contain the requested genre in their nested genre list
            recommendations = [movie for movie in movies if pref in movie[1]]
            
            if recommendations:
                print(f"\\n--- Recommendations for '{pref}' ---")
                display_movies(recommendations)
            else:
                print(f"No movies found for genre: {pref}")
                
        elif choice == '3':
            break

if __name__ == "__main__":
    run_movie_recommender()
