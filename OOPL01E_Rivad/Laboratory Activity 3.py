#Class for book
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = "Available"

    def borrow_book(self): #function for borrowing books
        if self.status == "Available":
            self.status = "Borrowed"
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is already borrowed.')

    def return_book(self): #function for returning booksS
        if self.status == "Borrowed":
            self.status = "Available"
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" is already available')

#Initialization
book1 = Book("Tamen de Gushi", "tan Jiu", 2014)
book2 = Book("Diary of a Wimpy Kid", "Greg Heffley", 2007)
book3 = Book("Harry Potter and the Chamber of Secrets", "J. K. Rowling", 1998)
book4 = Book("Noli Me Tangere", "Jose Rizal", 1887)

# List of books
books = [book1, book2, book3, book4]

# Function to display all books
def display_books():
    print("Books:")
    for index, book in enumerate(books, start=1):
        status = "(Available)" if book.status == "Available" else "(Borrowed)"
        print(f'{index}. {book.title} by {book.author} {status}')

# Function to borrow a book by its index
def choose_book_to_borrow():
    display_books()
    choice = int(input("Enter the number of the book you want to borrow: "))
    if 1 <= choice <= len(books):
        books[choice - 1].borrow_book()
    else:
        print("Invalid choice, please try again.")

# Function to return a book by its index
def choose_book_to_return():
    display_books()
    choice = int(input("Enter the number of the book you want to return: "))
    if 1 <= choice <= len(books):
        books[choice - 1].return_book()
    else:
        print("Invalid choice, please try again.")

# Borrow a book chosen by the user
choose_book_to_borrow()

# Return a book chosen by the user
choose_book_to_return()