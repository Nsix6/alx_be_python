class Book:
    """Just a regular book"""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author} published in {self.year}"
    
    def __del__(self):
        """Destructor for the book"""
        print(f"Deleting {self.title}")
    
    def __repr__(self):
        """Official string representation of the book"""
        return f"Book('{self.title}', '{self.author}',{self.year})"