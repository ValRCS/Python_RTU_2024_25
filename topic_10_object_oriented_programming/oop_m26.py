# let's talk about Object Oriented Programming
# Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.
# Idea is to bundle data and methods that operate on that data into a single unit called an object.
# Objects are instances of classes, which are blueprints for creating objects.

# Turns out pretty much everything is Python is class based.
# Even functions are objects, and classes are objects too.
# So, in Python, everything is an object, and everything has a type.
# Let's print some types of some primitive data types.
print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type("1")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type([])) # <class 'list'>
print(type({})) # <class 'dict'>

# so first let's see how we could create an application without classes
# we have a collection of books, and we want to store them in a list
# each book has a title, an author, and a year of publication, genre, and a rating
# let's create a list of books, where each book is a dictionary

book = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year": 1979,
    "genre": "Science Fiction",
    "rating": 4.5
}
book2 = {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951,
    "genre": "Fiction",
    "rating": 4.0
}

book3 = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960,
    "genre": "Fiction", 
    "rating": 4.3
}

latvian_book = {
    "title": "Mērnieku laiki",
    "author": "Kaudzītis Matīss un Kaudzīte Reinis",
    "year": 1879,
    "genre": "Fiction",
    "rating": 4.5
}
# now we can create a list of books
books = [book, book2, book3, latvian_book]

# now to do anything we should create functions

# let's create a function that prints title and author of the book
def print_book(book):
    print(f"{book['title']} by {book['author']} ({book['year']})")
    print(f"Genre: {book['genre']}")
    print(f"Rating: {book['rating']}")
    print()

print_book(latvian_book)

# let's create a function that changes rating of the book
def change_rating(book, new_rating):
    book['rating'] = new_rating
    print(f"Rating of {book['title']} changed to {book['rating']}")
    return book
change_rating(latvian_book, 5.0)
print_book(latvian_book)

# the issue is with above approach that these functions are outside the book
# so we have a generic dictionary, and we have to remember what keys are there
# and we have to find out which function to use for which dictionary
# and we have to pass the dictionary to the function every time

# so let's create a SimpleBook class to represent a simple version of book with only title and author and year\
# and we will create a method to print the book

class SimpleBook:
    # we could have some common attribut for all books
    # so let's say most books are made from paper
    # so we could have a class variable that is shared between all objects of the class
    material = "paper" # this is a class variable, and it is shared between all objects of the class

    # so __init__ is a special method that is called when we create an object of the class
    # it is used to initialize the object with some values
    # __ methods are called dunder methods, which are special methods in Python
    # full list of them is here: https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __init__(self, title, author, year):
        # so self is a reference to the current object, and we can use it to access the attributes of the object
        print("Creating a new book")
        self.title = title # it is typical to use same name as the parameter name
        # but we can use any name we want, but it is not recommended
        self.author = author
        self.year = year
        print(f"Book {self.title} by {self.author} ({self.year}) created")
        print("This book is made of", self.material)

# so this is user defined method, and it is not a special method
# could be called anything we want
    def print_book(self):
        print(f"{self.title} by {self.author} ({self.year})")

# so once we have a class we can create an object of that class
# and we can call the method on that object
# i will overwrite old book variable with a new object of SimpleBook class
book = SimpleBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book.print_book()


# let's make another book object
book2 = SimpleBook("The Catcher in the Rye", "J.D. Salinger", 1951)
book2.print_book()

# now we have two objects of the same class, and we can call the method on both objects

# note we have direct access to the attributes of the object, and we can change them directly
# but it is not recommended to do so, because it breaks the encapsulation principle of OOP

# for example I could change publication year of the book directly
book.year = 2000
print(book.year) # 2000

# even worse we can add any new attribute to the object, and it will be added to the object
# but it will not be added to the class, so it is not recommended to do so
book.reviewer = "Valdis"
print(book.reviewer) # Valdis
# note second book does not have this attribute, because it is not part of the class!
# so it would be better to add it to class in __init__ method
try:
    print(book2.reviewer) # this will raise an error, because book2 does not have this attribute
except AttributeError as e:
    print(e)

# so let's make a more complete class called Book
# that will have all the attributes of the book, and we will add some methods to it
# we will also add some setters and getters to the class

class Book:
    # we could have some common attribute for all books
    # so let's say most books are made from paper
    # so we could have a class variable that is shared between all objects of the class
    material = "paper" # this is a class variable, and it is shared between all objects of the class
    # of course each object can change this variable, but it is not recommended to do so

    def __init__(self, title="", author="", year=None, genre="fiction", rating=0):
        print("Creating a new book")
        self.title = title # it is typical to use same name as the parameter name
        # but we can use any name we want, but it is not recommended
        self.author = author
        self.year = year
        self.genre = genre
        self.rating = rating
        print(f"Book {self.title} by {self.author} ({self.year}) created")
        print("This book is made of", self.material)

    # let's also create a __str__ method to print the book object
    # only requirement is that it should return a string
    # this method is called when we use print on the object
    def __str__(self):
        # so we can return a string representation of the object
        # this is called string representation of the object
        # and it is used when we print the object
        # mistake would be to try to print the object directly here
        return f"BOOK: {self.title} by {self.author} ({self.year})"
    

    # let's add one more dunder method
    # let's add greater than method to compare books by rating
    # this method is called when we use > operator on the object
    # so we can compare books by rating
    def __gt__(self, other) -> bool:
        # so we can compare books by rating
        # this is called greater than method
        # and it is used when we use > operator on the object
        # so we can compare books by rating
        if not isinstance(other, Book):
            return NotImplemented

        return self.rating > other.rating # we could of course use more complex logic
    
    # similarly I could add less than method to compare books by rating and so on
    # full list of dunder methods is here: https://docs.python.org/3/reference/datamodel.html#special-method-names

    def print_book(self):
        print(f"{self.title} by {self.author} ({self.year})")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}")
        # so if we return nothing it might make sense to return self
        return self
        # this way we can chain the methods together

    # let's make a method to adjust rating
    def set_rating(self, new_rating):
        # this lets us set some business logic to the setter
        # for example we could check if the rating is between 0 and 5
        if new_rating < 0 or new_rating > 5:
            print("Rating should be between 0 and 5")
            return
        self.rating = new_rating
        print(f"Rating of {self.title} changed to {self.rating}")
        # again returning self lets us chain the methods together
        return self

    # let's add method to adjust rating by some value
    def adjust_rating(self, delta):
        # this lets us set some business logic to the setter
        # for example we could check if the rating is between 0 and 5
        if self.rating + delta < 0 or self.rating + delta > 5:
            print("Rating should be between 0 and 5")
            # we could use floor or ceil to set the rating to 0 or 5
            # but we will just return and not change the rating
            return
        self.rating += delta
        print(f"Rating of {self.title} changed to {self.rating}")
        # again returning self lets us chain the methods together
        return self

    # let's make a set year method
    def set_year(self, new_year):
        # this lets us set some business logic to the setter
        # for example we could check if the year is a number
        if not isinstance(new_year, int):
            print("Year should be a number")
            return
        self.year = new_year
        print(f"Year of {self.title} changed to {self.year}")
        # again returning self lets us chain the methods together
        return self

# now I can create a blank book object, and I can set the attributes later
book = Book() # uses ALL default values
# I can also make a book with just title and author
book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2.print_book()

# i could make a book where only year is known
book3 = Book(year=1984)
book3.print_book()

# let's set rating of the book to 4.5
book2.set_rating(4.5)
book2.set_year(1979)
book2.print_book()
# let's adjust rating by 0.4
book2.adjust_rating(0.4)
book2.print_book()
# let's adjust rating by -5.0
book2.adjust_rating(-5.0)
book2.print_book()

# now that we return self for many methods we can chain the methods together
# so we can do this:
book.print_book().set_rating(4.5).adjust_rating(0.2).set_year(2000).print_book()
# this is called method chaining, and it is a common pattern in OOP
# in Python you will see libraries such as Pandas and SQLAlchemy using this pattern a lot
# so we can create a list of books, and we can use the methods on the objects in the list

# let's try print on book object
print(book2) 
# without __str_ method it will print the object reference, which is not very useful

# let's print ratings of both books first
print(f"Rating of book 1: {book.rating}")
print(f"Rating of book 2: {book2.rating}")

# now we can compare two books by rating using > operator
print(f"Is book 1 better than book 2? {book > book2}") 
# without __gt__ we would have had to do it directly by comparing the rating attribute
print(f"Is book 1 better than book 2? {book.rating > book2.rating}")
