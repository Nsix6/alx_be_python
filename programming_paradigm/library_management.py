class Book:
    """A class representing a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    
    def return_book(self):
        """Return the book to the library."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self.__is_checked_out
    

class Library:
    """A class representing a library."""
    def __init__(self, books=None):
        self.__books = books if books is not None else []

    def add_book(self, book):
        """add a book to the library."""
        self.__books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library by title."""
        for book in self.__books:
            if book.title in title and not book._Book__is_checked_out:
                book._Book__is_checked_out = True
                print(f"Available books after checking out '{book.title}':")
                self.list_available_books()
                return True
        return False
        
    def return_book(self, title):
        """Returns a book by title."""
        for book in self.__books:
            if book.title == title and book.is_available():
                book.return_book()
                print(f"Available books after returning '{book.title}':")
                self.list_available_books()
                return True
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self.__books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        return available_books