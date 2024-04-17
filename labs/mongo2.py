import pymongo

class Book:
    def __init__(self, title, author, isbn, publisher, publication_year, genre, page_count, language):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre
        self.page_count = page_count
        self.language = language

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'publisher': self.publisher,
            'publication_year': self.publication_year,
            'genre': self.genre,
            'page_count': self.page_count,
            'language': self.language
        }

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Connect to the MongoDB server running on default port 27017
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Create or switch to a database
db = client['Library']

# Create a new collection or get an existing collection
books = db['Books']

books_data = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780446310789", "publisher": "J.B. Lippincott & Co.", "publication_year": 1960, "genre": "Fiction", "page_count": 281, "language": "English"},
    {"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "publisher": "Secker & Warburg", "publication_year": 1949, "genre": "Dystopian", "page_count": 328, "language": "English"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "9780743273565", "publisher": "Charles Scribner's Sons", "publication_year": 1925, "genre": "Fiction", "page_count": 180, "language": "English"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "9780679783268", "publisher": "T. Egerton, Whitehall", "publication_year": 1813, "genre": "Romance", "page_count": 279, "language": "English"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "9780316769488", "publisher": "Little, Brown and Company", "publication_year": 1951, "genre": "Fiction", "page_count": 234, "language": "English"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "9780547928227", "publisher": "George Allen & Unwin", "publication_year": 1937, "genre": "Fantasy", "page_count": 310, "language": "English"},
    {"title": "The Book Thief", "author": "Markus Zusak", "isbn": "9780375842207", "publisher": "Picador", "publication_year": 2005, "genre": "Historical Fiction", "page_count": 552, "language": "English"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "isbn": "9781451673319", "publisher": "Ballantine Books", "publication_year": 1953, "genre": "Dystopian", "page_count": 249, "language": "English"},
    {"title": "Brave New World", "author": "Aldous Huxley", "isbn": "9780060850524", "publisher": "Chatto & Windus", "publication_year": 1932, "genre": "Dystopian", "page_count": 311, "language": "English"},
    {"title": "Moby Dick", "author": "Herman Melville", "isbn": "9780142437247", "publisher": "Richard Bentley", "publication_year": 1851, "genre": "Adventure", "page_count": 635, "language": "English"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "isbn": "9780307266934", "publisher": "The Russian Messenger", "publication_year": 1869, "genre": "Historical Fiction", "page_count": 1225, "language": "English"},
    {"title": "Lolita", "author": "Vladimir Nabokov", "isbn": "9780679723165", "publisher": "Olympia Press", "publication_year": 1955, "genre": "Fiction", "page_count": 336, "language": "English"},
    {"title": "Catch-22", "author": "Joseph Heller", "isbn": "9781451626650", "publisher": "Simon & Schuster", "publication_year": 1961, "genre": "Satire", "page_count": 453, "language": "English"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "isbn": "9780544003415", "publisher": "Allen & Unwin", "publication_year": 1954, "genre": "Fantasy", "page_count": 600,"language": "English"}
]



# Welcome message
print("--- Hello and welcome to the awesome Lexicon bookstore! ---")
def main_menu():
    print("\nChoose an option:")
    print("1: Add a book")
    print("2: View all books")
    print("3: Search a book by title")
    print("4: Update a book price")
    print("5: Delete a book")
    print("6: View books by author")
    print("7: View books in Stock")
    print("8: Exit")
    return input("Enter choice: ")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    price = float(input("Enter the price of the book: "))
    in_stock = input("Is the book in stock (yes/no)? ").lower() == 'yes'
    book = {"title": title, "author": author, "isbn": isbn, "price": price, "in_stock": in_stock}
    books.insert_one(book)
    print("Book added successfully!")

def view_all_books():
    for book in books.find():
        print(book)

def search_book_by_title():
    title = input("Enter the title of the book to search: ")
    book = books.find_one({"title": title})
    if book:
        print(book)
    else:
        print("No book found with that title.")
    

    
def update_book_price():
    title = input("Enter the title of the book to update: ")
    new_price = float(input("Enter the new price: "))
    result = books.update_one({"title": title}, {"$set": {"price": new_price}})
    if result.modified_count:
        print("Updated successfully!")
    else:
        print("No book was updated.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    result = books.delete_one({"title": title})
    if result.deleted_count:
        print("Book deleted successfully!")
    else:
        print("No book was deleted.")

def view_books_by_author():
    author = input("Enter the author's name: ")
    for book in books.find({"author": author}):
        print(book)

def view_books_in_stock():
    for book in books.find({"in_stock": True}):
        print(book)

def main():
    while True:
        user_choice = main_menu()
        if user_choice == "1":
            add_book()
        elif user_choice == "2":
            view_all_books()
        elif user_choice == "3":
            search_book_by_title()
        elif user_choice == "4":
            update_book_price()
        elif user_choice == "5":
            delete_book()
        elif user_choice == "6":
            view_books_by_author()
        elif user_choice == "7":
            view_books_in_stock()
        elif user_choice == "8":
            print("Thank you for using the bookstore system!")
            break
        else:
            print("Invalid choice, please try again.")


main()