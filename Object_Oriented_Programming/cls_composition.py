class BookShelf:
    def __init__(self, quantity):
        self.books = quantity

    def __str__(self):
        return f"BookShelf with {self.books} books."


shelf = BookShelf(300)
print(shelf)