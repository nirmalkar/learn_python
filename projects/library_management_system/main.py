from book import Book
from member import Member
from library import Library

if __name__ == "__main__":
    library = Library("Monty's Library")

    book1 = Book("Getting things done", "David Allen", "123456789")
    book2 = Book("The Power of Subconcious Mind", "Josheph Murphy", "987654321")
    library.add_book(book1)
    library.add_book(book2)

    member1 = Member("Hemant", 1)
    member2 = Member("Ravi", 2)
    library.add_member(member1)
    library.add_member(member2)

    print("All books in the library:")
    library.display_books()

    print("\nAll members of the library:")
    library.display_members()

    print("\nLending a book:")
    library.lend_book_to_member("123456789", 1)
    
    library.lend_book_to_member("123456789", 2)

    print("\nReturning a book:")
    library.return_book_from_member("123456789", 1)

    print("\nAll books in the library after lending and returning:")
    library.display_books()

    print("\nAll members of the library after lending and returning:")
    library.display_members()
