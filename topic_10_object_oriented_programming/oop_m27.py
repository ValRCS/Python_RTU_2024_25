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

# now let's make a bigger class with more attributes and methods
# let's make a class called Book with more attributes and methods

# this class will have attributes - data and methods - functions for working with the data
class Book:
    # this is a special method that is called when we create an object of the class
    # it is used to initialize the attributes of the class
    def __init__(self, title="", 
                 author="", 
                 year=None, 
                 genre=None, 
                 pages=0, 
                 publisher=None):
        print("Creating a new book object")
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.publisher = publisher
        # print(f'Book object created with title: {self.title} and author: {self.author}')
        print("Created a new book object")
        # i can call my other methods here
        self.print_info() # so methods know about each other

    # let's define one more special method - __str__
    # this method is called when we print the object
    # only requirement is that __str__ returns a string
    def __str__(self):
        # this method will return a string representation of the object
        # this is what will be printed when we print the object
        return f'Book Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Pages: {self.pages}, Publisher: {self.publisher}'
    
    # full list of dunder methods is here https://docs.python.org/3/reference/datamodel.html#special-method-names

    # kind of silly example 
    # but let's define __add__ for our class
    # this method is called when we use the + operator on the objects of the class
    # we will will add or concatanate all attributes of the two books
    def __add__(self, other):
        # this method will return a new object of the class Book with the attributes of the two books added together
        # this is not a very useful method but it is just an example of how to use __add__
        # we will add the title and author together and return a new object of the class Book
        new_title = self.title + " & " + other.title
        new_author = self.author + " & " + other.author
        new_year = self.year + other.year if self.year and other.year else None
        new_genre = self.genre + " & " + other.genre if self.genre and other.genre else None
        new_pages = self.pages + other.pages if self.pages and other.pages else 0
        new_publisher = self.publisher + " & " + other.publisher if self.publisher and other.publisher else None
        
        return Book(new_title, new_author, new_year, new_genre, new_pages, new_publisher)

    # this method will print the book info
    def print_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Pages: {self.pages}, Publisher: {self.publisher}')
        # let's add return self to all methods that return None
        # we will gain chaining of methods
        # so we can call the methods one after another
        return self

    # let's define a method to change publisher of the book
    def change_publisher(self, new_publisher, verbose = False):
        # this method will change the publisher of the book
        # here we could add some extra logic to check if publisher is valid or not
        self.publisher = new_publisher
        if verbose:
            print(f'Publisher changed to: {self.publisher}')
        return self

    # let's make a set year method
    def set_year(self, year):
        # this method will set the year of the book
        # here we could add some extra logic to check if year is valid or not
        self.year = year
        return self

    # let's make a method to add year to the book
    def add_year(self, years=1):
        # this method will add years to the year of the book
        # here we could add some extra logic to check if years is valid or not
        if self.year:
            self.year += years
        # again return self to gain chaining of methods
        return self


# let's create a new book
wizard_of_oz = Book('The Wizard of Oz', 'L. Frank Baum', 1900, 'Fantasy', 154, 'George M. Hill Company')
# wizard_of_oz.print_info() # Title: The Wizard of Oz, Author: L. Frank Baum, Year: 1900, Genre: Fantasy, Pages: 154, Publisher: George M. Hill Company
spriditis = Book('Spriditis', 'Anna Brigadere', 1912, 'Fantasy', 200, 'Zvaigzne ABC')
# spriditis.print_info() # Title: Spriditis, Author: Anna Brigadere, Year: 1912, Genre: Fantasy, Pages: 200, Publisher: Zvaigzne ABC

# now let's see what happens if I print spriditis
# by default the information is not very useful - it is some memory address
# this is because the class does not have a __str__ method defined
print(spriditis) # <__main__.Book object at 0x7f8c3c0e5d90>

# now I can make a franken book by adding the two books together
franken_book = wizard_of_oz + spriditis

# so key with dunder methods is that they are called automatically by Python when we use certain operations on the objects of the class
# we want to make them semantically correct and useful

# now we might want to modify some data in the class
# we could do this directly but this is not a good practice
# instead let's define some methods to modify the data in the class
# this is called encapsulation - we want to hide the data from the outside world and provide methods to access and modify the data

# let's change the publisher
spriditis.change_publisher('Zvaigzne ABC', True) # Publisher changed to: Zvaigzne ABC

# let's set year to 2020
spriditis.set_year(2020)
# now let's print the book info again
spriditis.print_info() # Title: Spriditis, Author: Anna Brigadere, Year: 2020, Genre: Fantasy, Pages: 200, Publisher: Zvaigzne ABC

# let's add 5  years to book
spriditis.add_year(5) # so technically same as spriditis.year += 5
# now let's print the book info again
spriditis.print_info() # Title: Spriditis, Author: Anna Brigadere, Year: 1917, Genre: Fantasy, Pages: 200, Publisher: Zvaigzne ABC


# now that I've added return self to all methods I can chain the methods together
# this is called method chaining - we can call the methods one after another
# so I can do this:
wizard_of_oz.print_info().change_publisher('Zvaigzne ABC').set_year(1984).add_year(5).print_info()
# this will change the publisher, set the year and add 5 years to the year and print the book info