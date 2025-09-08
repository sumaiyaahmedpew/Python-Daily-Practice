#35 Library with inner class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return f"{self.title} by {self.author}"

    def add_book(self, title, author):
        book = self.Book(title, author)
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                print(book)

    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


if __name__ == "__main__":
    lib = Library("City Library")
    lib.add_book("Python Crash Course", "Eric Matthes")
    lib.add_book("Learning Python", "Mark Lutz")

    lib.show_books()

    res = lib.search("Python Crash Course")
    print("Search Result:", res)
