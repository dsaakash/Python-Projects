"""
Beginner Project 5: Favourite Books
Concepts: List sorting (sort(), sorted()), reversing (reverse()).
"""

def run_book_manager():
    books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "Harry Potter"]
    
    print("--- Favourite Books Library ---")
    print("Original List:")
    print(books)
    
    print("\\n1. Alphabetical Order using sorted() (Creates a new list):")
    sorted_books = sorted(books)
    print(sorted_books)
    print("Notice the original list is unchanged:", books)
    
    print("\\n2. Alphabetical Order using sort() (Modifies original list):")
    books.sort()
    print(books)
    
    print("\\n3. Reverse Alphabetical Order:")
    books.sort(reverse=True)
    print(books)
    
    print("\\n4. Reversing the current list order using reverse():")
    books.reverse()
    print(books)
    
    print("\\nAdding a new book to the end and re-sorting...")
    books.append("The Hobbit")
    books.sort()
    print("Final Library:", books)

if __name__ == "__main__":
    run_book_manager()
