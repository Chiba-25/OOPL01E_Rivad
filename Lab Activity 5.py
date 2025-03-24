# Book class definition
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

# Library class definition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def display_books(self):
        print("\nBooks in Library:")
        for idx, book in enumerate(self.books, 1):
            status = "Available" if book.is_available else "Not Available"
            print(f"{idx}. {book.title} - {status}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            return found_books[0]
        else:
            print(f"Book titled '{title}' not found.")
            return None

# Implementing the Library Management System
library = Library()

# Creating books
book1 = Book("Diary of a Wimpy Kid", "Jeff Kinney", "9780143303831")
book2 = Book("My Hero Academia, Vol. 1", "Horikoshi Kouhei", "9789863824978")
book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9788869183157")

# Adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# User interaction loop
while True:
    print("\nLibrary Menu:")
    print("1. Display Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Search for a Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input("Enter the title of the book to borrow: ")
        book_to_borrow = library.search_book(title)
        if book_to_borrow:
            book_to_borrow.borrow_book()
    elif choice == '3':
        title = input("Enter the title of the book to return: ")
        book_to_return = library.search_book(title)
        if book_to_return:
            book_to_return.return_book()
    elif choice == '4':
        title = input("Enter the title of the book to search for: ")
        book_found = library.search_book(title)
        if book_found:
            status = "Available" if book_found.is_available else "Not Available"
            print(f"Found: {book_found.title} by {book_found.author} - {status}")
    elif choice == '5':
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
