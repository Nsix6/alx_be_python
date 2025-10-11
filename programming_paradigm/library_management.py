class Book:
    """A class representing a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

class Library:
    """A class representing a library."""
    def __init__(self, books=None):
        try:
            if books is None:
                self.__books = []
            else:
                print("Available books after setup:")
                self.__books = books
        except Exception as e:
            print(f"An error occurred while initializing the library: {e}")
            self.__books = []

    def add_book(self, book):
        """add a book to the library."""
        self.__books.append(book)

    def check_out_books(self, title):
        """Check out a book from the library by title."""
        try:
            for book in self.__books:
                if book.title in title and not book._Book__is_checked_out:
                    book._Book__is_checked_out = True
                    print(f"Available books after checking out '{book.title}':")
                    self.list_available_books()
                    return True
            return False
        except Exception as e:
            print(f"An error occurred while checking out the book: {e}")
            return False
        
    def return_book(self, title):
        """Returns a book by title."""
        try:
            for book in self.__books:
                if book.title in title and book._Book__is_checked_out:
                    book._Book__is_checked_out = False
                    print(f"Available books after returning'{book.title}':")
                    self.list_available_books()
                    return True
            return False
        except Exception as e:
            print(f"An error occurred while returning the book: {e}")
            return False
    
    def list_available_books(self):
        """List all available books in the library."""
        try:
            available_books = [book for book in self.__books if not book._Book__is_checked_out]
            if not available_books:
                print("No books are currently available.")
            else:
                for book in available_books:
                    print(f"{book.title} by {book.author}")
            return available_books
        except Exception as e:
            print(f"An error occurred while listing available books: {e}")
            return []