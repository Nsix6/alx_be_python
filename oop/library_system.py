class Book:
    """Just a regular book"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"

    
class EBook(Book):
    """An electronic book"""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of the eBook"""
        return f"EBook: {self.title} by {self.author}, file size: {self.file_size}KB"



class PrintBook(Book):
    """A printed book"""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    


class Library:
    """A simple library system"""
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
    
    def list_books(self):
        """List all books in the library"""
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            print(book)