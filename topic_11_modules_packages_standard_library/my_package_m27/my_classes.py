# let's create a simple class to test our module
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

# I could add a main guard here, but it is not necessary if I have no code to run
# if __name__ == "__main__":
#     # this is just for testing purposes
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
#     book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)