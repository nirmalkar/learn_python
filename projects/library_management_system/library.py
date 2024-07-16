from typing import List, Optional
from book import Book
from member import Member

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, book:Book) -> None:
        self.books.append(book)

    def display_books(self) -> None:
        for book in self.books:
            print(book.display_info())

    def add_member(self, member:Member) -> None:
        self.members.append(member)
    
    def lend_book_to_member(self, isbn: str, member_id: int) -> None:
        book: Optional[Book] = next((b for b in self.books if b.isbn == isbn and not b.is_lent), None)
        member: Optional[Member] = next((m for m in self.members if m.member_id == member_id), None)
        if book and member:
            if member.borrow_book(book):
                print(f"Book '{book.title}' lent to member '{member.name}'")
            else:
                print(f"Book '{book.title}' is already lent out")
        else:
            print("Book or member not found")

    def return_book_from_member(self, isbn: str, member_id: int) -> None:
        book: Optional[Book] = next((b for b in self.books if b.isbn == isbn), None)
        member: Optional[Member] = next((m for m in self.members if m.member_id == member_id), None)
        if book and member:
            if member.return_book(book):
                print(f"Book '{book.title}' returned by member '{member.name}'")
            else:
                print(f"Book '{book.title}' was not borrowed by member '{member.name}'")
        else:
            print("Book or member not found")

    def display_members(self) -> None:
        for member in self.members:
            print(member.display_info())