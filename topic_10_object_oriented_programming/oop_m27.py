# Let's talk about core tenets of OOP - Object Oriented Programming
# Main idea is to bundle data and functionality together
# We use classes to define the structure of our objects - basically a blueprint
# or template for creating objects
# then we use this class (blueprint, template) to create objects (instances of the class)

# first let's see how our life is without classes and objects

# let's say I have a library and I want to keep track of the books in my library
# let's say I will have a list of dictionaries where each dictionary will represent a book
# and the keys of the dictionary will be the attributes of the book
sample_book = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'year': 1925,
    'genre': 'Fiction',
    'pages': 180,
    'publisher': 'Scribner'
}

books = []
books.append(sample_book)

# now I get tired of using append and I want to add a new book to my library
# I could make a function to add this book
# good practice would be to take in the old dictionary, then parameters of the book and return a dictionary

def add_book(books, title, author=None, year=None, genre=None, pages=0, publisher=None):
    """
    IN PLACE addition of a book to the list of books
    :param books: list of books
    :param title: title of the book
    :param author: author of the book
    :param year: year of publication
    :param genre: genre of the book
    :param pages: number of pages in the book
    :param publisher: publisher of the book
    :return: original list of books with the new book added
    """
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'pages': pages,
        'publisher': publisher
    }
    books.append(book)
    return books # I return the same list with the new book added to it

# let's add Lelde's Kovaļovas book to the library
# add_book(books, 'Lelde Kovaļova', 'Klusie Kaimiņi', 2023, 'Fiction', 300, 'Zvaigzne ABC')
# print(books)

# now I could add more functions to provide statistics about the books in the library
# for example, I could add a function to get the number of books in the library

# the issue is that data is separated from the functionality - functions are not related to the data

# so instead of dictionary for storing book data let's use class based approach

# let's create a class called Book
# this class will have attributes - data and methods - functions for working with the data

# for now let's create a very SimpleBook class with just a title and an author
# and a method to print the book info

class SimpleBook: # so class is a template for my objects - books here
    # __init__ is a special method that is called when we create an object of the class
    # it is used to initialize the attributes of the class
    # this method is called when we create an object of the class
    # self is a reference to the current object - it is used to access the attributes and methods of the class
    def __init__(self, title="", author=""):
        self.title = title
        self.author = author

    # this method I made up myself - it is not a special method
    # it is just a regular method that I defined to print the book info
    def print_info(self): # again self is mandatory here
        # this method will print the title and author of the book
        print(f'Title: {self.title}, Author: {self.author}')

# now I've defined a class but I haven't created any objects yet
gatsby = SimpleBook('The Great Gatsby', 'F. Scott Fitzgerald')
# i've created an object of the class SimpleBook called gatsby this is an instance of the class
gatsby.print_info() # Title: The Great Gatsby, Author: F. Scott Fitzgerald
# note I did not need to use self here - self is used only in the class definition

artofdeal = SimpleBook('The Art of Deal', 'Donald Trump')
artofdeal.print_info() # Title: The Art of Deal, Author: Donald Trump
# i can print the title also directly
print(f"Title: {artofdeal.title}") # Title: The Art of Deal

# now that I've created default values for the attributes I can create an object without passing any arguments
blank_book = SimpleBook() # this will create an object with empty title and author
blank_book.print_info() # Title: , Author:
# Python is very liberal and loose
# so I can change the attributes of the object after I've created it
# this is called dynamic typing - I can change the type of the attribute at any time
blank_book.title = 'Harry Potter'
blank_book.author = 'J.K. Rowling'
# in strict languages like Java I would have to define the type of the attribute in the class
# but in Python I can change the type of the attribute at any time
# also strict OOP languages do not like to have public attributes - they are private by default

# Python offers a way to hide some attributes from the outside world but about that later

# even crazier Python lets us add new attributes to the object at any time
blank_book.publisher = 'Bloomsbury'
blank_book.content = "This is a book about a wizard"
# above two attributes are completely new and were not defined in the class
# not the best practice but it is possible
# by using arbitrary attributes we lose a bit of the structure and safety of the class
# but this is also a feature of Python - it is very flexible and dynamic
blank_book.print_info() # Title: Harry Potter, Author: J.K. Rowling