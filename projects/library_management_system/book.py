class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_lent = False
    
    def lend_book(self) -> bool:
        if not self.is_lent:
            self.is_lent = True
            return True
        return False
    
    def return_book(self) -> bool:
        if  self.is_lent:
            self.is_lent = False
            return True
        return False
    
    def display_info(self) -> str:
        status = "Available" if not self.is_lent else "Lent Out"
        return f"Title: {self.title}, Author: {self.author}, Isbn: {self.isbn}, Status: {status}"
    

# book_one = Book("1984", "George Orwell", "123456789")
# print(book_one.display_info())
    