book_collection = {}


def add_book(title, author, genre, year):
    book_collection[title] = {"author": author, "genre": genre, "year": year}
    print("Book added successfully!")


def remove_book(title):
    if title in book_collection:
        del book_collection[title]
        print("Book removed successfully!")
    else:
        print("Book not found!")


def search_by_genre(genre):
    results = [book for book, details in book_collection.items() if details["genre"] == genre]
    return results


def search_by_author(author):
    results = [book for book, details in book_collection.items() if details["author"] == author]
    return results


def display_books():
    print("\nBook Collection:")
    for title, details in book_collection.items():
        print(f"Title: {title}")
        print(f"Author: {details['author']}")
        print(f"Genre: {details['genre']}")
        print(f"Year: {details['year']}")
        print("--------------------")


while True:
    print("\nBook Collection Manager")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search by Genre")
    print("4. Search by Author")
    print("5. Display All Books")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        year = input("Enter book year: ")
        add_book(title, author, genre, year)
    elif choice == "2":
        title = input("Enter book title to remove: ")
        remove_book(title)
    elif choice == "3":
        genre = input("Enter genre to search: ")
        results = search_by_genre(genre)
        if results:
            print(f"\nBooks in {genre} genre:")
            for title in results:
                print(title)
        else:
            print("No books found in this genre!")
    elif choice == "4":
        author = input("Enter author to search: ")
        results = search_by_author(author)
        if results:
            print(f"\nBooks by {author}:")
            for title in results:
                print(title)
        else:
            print("No books found by this author!")
    elif choice == "5":
        display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

