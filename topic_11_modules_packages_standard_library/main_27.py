# we usually import standard library modules at the top of the file
# so where does Python look for modules?
# let's find out by importing the sys module and printing the sys.path variable
import sys # sys is standard library module that provides access to system-specific parameters and functions# 
# full list of standard library modules can be found here: https://docs.python.org/3/library/index.html

# here we would import external modules if we had any


# finally we import our own modules
# this is my main program that will use modules from other files
import my_module_m27 # this will import the module and execute it
# we gain namespace my_module_m27 we can use to access the module
# we can use the module by prefixing it with the module name
# let's also import song_rap_m27 module
# import song_rap_m27 # this will import the module and execute it
# instead of importing the module, we can import specific classes or functions from the module
# from song_rap_m27 import Song, Rap # this will import the classes from the module
# above is a good approach if we have a huge module and don't want to import everything

# we have another popular approach to import modules - aliasing
import song_rap_m27 as srm # this will import the module and execute
# srm could be any name we want, but it is a good practice to use short and meaningful names
# now we have acces to shortened name srm to access the module
# we still keep namespaces separate

# we could also import individual classes or functions from the module and rename them
# from song_rap_m27 import Song as S, Rap as R # this will import the classes from the module
# this is not a good practice, because it makes the code less readable

# there is one very dangerous way to import modules - using from module import *
# this will import everything from the module into the current namespace
# BAD PRACTICE - it will overwrite any existing variables with the same name

# so modules offer us the following benefits:
# 1. code reusability - we can use the same module in different programs
# 2. code organization - we can organize our code into different modules
# 3. code testing - we can test our modules separately from the main program
# 4. code encapsulation - we can hide the implementation details of the module from the main program
# 5. code readability - we can make our code more readable by using modules
# 6. code maintainability - we can make our code more maintainable by using modules

# how about packages?
# packages are just directories that contain modules and sub-packages
# packages are a way to organize modules into a hierarchy

# so to use my_package_m27 package, we need to import it first
# we can import the whole package or specific modules from the package
# let's import the whole package
from my_package_m27 import my_math # this will import the module from the package

# let's import classes from my_classes module in my_package_m27 package
from my_package_m27.my_classes import Book, Library # this will import the classes from the module


def main(): # In Python main() is not required, but it is a good practice to use 
    print("This is the main program")
    print("It will use modules from other files")
    print(f"Our module search path is: {sys.path}")
    # we can see that the first entry is the current directory
    # this means we have to be a bit careful with naming our own modules
    # we should not reuse names of standard library modules
    # otherwise we might get unexpected results


    print(my_module_m27.my_list) # this will print the list from the module
    print(my_module_m27.my_string) # this will print the string from the module
    print(my_module_m27.my_dict) # this will print the dictionary from the module
    print(my_module_m27.add(2, 3)) # this will print the result of the add funct

    # now we can create a song object from the song_rap_m27 module
    ziemelmeita = srm.Song("Ziemelmeita", "Jumprava", ("Ziemelmeita, Ziemelmeita", "Tu esi manā sirdī", "Tu esi manā dvēselē", "Tu esi manā dzīvē"))
    ziemelmeita.sing(2).yell(1) # chaining

    # I can also make a Rap - say Eminem
    rapper = srm.Rap("Rap God", "Eminem", ["I'm beginning to feel like a Rap God, Rap God",
                                "All my people from the front to the back nod, back nod",
                                "Now who thinks their arms are long enough to slap box, slap box?"])
    rapper.break_it(2, "yo").yell(1) # chaining

    print(my_math.add(2, 3)) # this will print the result of the add function from my_package_m27 package
    print(my_math.subtract(5, 3)) # this will print the result of the subtract function from my_package_m27 package

    gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(gatsby) # this will print the book object using the __str__ method from the Book class
    zelta_riga = Book("Zelta Rīga", "Jānis Jaunsudrabiņš", 1930) # fake!
    print(zelta_riga) # this will print the book object using the __str__ method from the Book class

    my_library = Library()
    my_library.add_book(gatsby) # this will add the book to the library
    my_library.add_book(zelta_riga) # this will add the book to the library
    my_library.show_books() # this will show the books in the library



# typically we would start the program here
# first we will check if program is started directly or imported
if __name__ == "__main__":
    # we could add say config() here
    main()
    # also maybe a function called cleanup() to clean up the program