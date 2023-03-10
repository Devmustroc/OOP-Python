class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

    def get_books(self):
        bks = [book.name for book in self.books]
        return bks

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry potter")
book2 = Book("Python 101")
book3 = Book("Game of thrones")
shelf = BookShelf(book, book2, book3)
print(shelf)
print(shelf.get_books())