from typing import List
from book import Book

class Member:
    def __init__(self, name:str, member_id:int) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books: List[Book] = []

    def borrow_book(self, book:Book) -> bool:
        if book.lend_book():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book:Book) -> bool:
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False
    
    def display_info(self) -> str:
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books])
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {borrowed_titles if borrowed_titles else 'None'}"
