class Book:
    def __init__(self, name: str, pages_count: int):
        self.name = name
        self.pages_count = pages_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.pages_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.pages_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.pages_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.pages_count}")


python101 = Book("Python 101", 50)
python101.read(35)
python101.read(50)