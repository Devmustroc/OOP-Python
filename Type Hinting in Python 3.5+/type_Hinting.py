# type hinting is a way to tell the interpreter what type of data a function or variable is expecting
from typing import List # tuple, set, dict, etc...

# class Book:
#     pass
#
# class BookShelf:
#     def __init__(self, books: List[Book]):
#         self.books = books
#
#     def __str__(self) -> str:
#         return f"BookShelf with {len(self.books)} books."
#
#     def get_books(self):
#         bks = [book.name for book in self.books]
#         return bks


class Book:
    TYPE = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self) -> str:
        return f'Book {self.name}, {self.book_type}, weighing {self.weight}g'

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPE[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> 'Book':
        return cls(name, cls.TYPE[1], page_weight)
