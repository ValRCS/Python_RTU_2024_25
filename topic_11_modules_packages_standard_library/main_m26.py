# let's use my_module_m26.py in this snippet
# import my_module_m26 # note no need for .py extension
# alternative way to import is to use alias - mostly because the module name is long
# import my_module_m26 as mmm # it is common practice to use abbreviations for module names

# I have imported everything from my_module_m26.py
# I Can use the variables and functions defined in my_module_m26.py
# all I need is prefix the variable and function names with my_module_m26.

# print(my_module_m26.my_var)  # 42
# print(my_module_m26.my_list)  # [1, 2, 3, 4, 5]
# print(my_module_m26.my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(my_module_m26.my_add(5, 10))  # 15

# we can create the class template in my_module_m26.py to create an object in our main_m26.py file
# my_obj = my_module_m26.MyClass("Bob")
# print(my_obj.greet())  # Hello, Bob!

# so import is sort of like giant copy and paste
# but it is not exactly like that

# why are modules useful?

# 1. Code Reusability: You can reuse code across multiple programs without rewriting it.
# 2. Organization: Modules help organize code into logical sections, making it easier to read and maintain.
# 3. Namespacing: Modules create a separate namespace, preventing naming conflicts between variables and functions.
# 4. Collaboration: Multiple developers can work on different modules simultaneously, improving teamwork and productivity.
# 5. Standard Library: Python comes with a rich standard library of modules that provide pre-built functionality for common tasks, such as file I/O, networking, and data manipulation.

# now if I used alias to import my_module_m26.py, I can use the alias to access the variables and functions
# print(mmm.my_var)  # 42
# print(mmm.my_list)  # [1, 2, 3, 4, 5]
# print(mmm.my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(mmm.my_add(5, 10))  # 15


# where does Python look for modules to import?
# let's see this in the next snippet
import sys # this is a built-in module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
print(f"sys.path: {sys.path}") # this is a list of strings that specifies the search path for modules. It is initialized from the PYTHONPATH environment variable, plus an installation-dependent default.

# if we really want we can add our own directories to the sys.path list
# let's add parent directory to the sys.path list
# let's use pathlib to get the parent directory
from pathlib import Path # again standard library module
# this is a built-in module that provides classes representing filesystem paths with semantics appropriate for different operating systems.
parent_dir = Path(__file__).resolve().parent.parent # this will give us the parent directory of the current file
print(f"parent_dir: {parent_dir}") # this will give us the parent directory of the current file
# let's add the parent directory to the sys.path list
sys.path.append(str(parent_dir)) # we need to convert the Path object to string
print(f"sys.path: {sys.path}") # this will give us the updated sys.path list

# how about sibling directory such as topic_10_object_oriented_programming
# let's add the sibling directory to the sys.path list
# let's use pathlib to get the sibling directory
sibling = Path("topic_10_object_oriented_programming").resolve() # this will give us the sibling directory of the current file
print(f"sibling: {sibling}") # this will give us the sibling directory of the current file
# let's add the sibling directory to the sys.path list
sys.path.append(str(sibling)) # we need to convert the Path object to string
print(f"sys.path: {sys.path}") # this will give us the updated sys.path list

# Now I can import song_rap_m26.py from topic_10_object_oriented_programming directory
import song_rap_m27 # this will import the song_ramp_m26.py file from topic_10_object_oriented_programming directory

# now I can use it to create song object
my_song = song_rap_m27.Song("Īssavienojums","Prāta Vētra", ("Cik dīvainas ir tās paralēles", "Kas ved mūs pa takām kalnā", "Un kad tu mani trīsreiz piekrāpsi", "Es pazudīšu ar salnām", "Tad stāvēšu dzelzceļa malā", "Turp atpakaļ vilcienus vērot","Rītdiena nekad nepienāks", "Džeimsam nav, par ko sērot"))
my_song.yell(2).sing(3) # chaining

# more on importing I could just import a single function or class
# from my_module_m26  import my_add, MyClass # this will import only the my_add function from my_module_m26.py file
# # now I can use it without prefixing it with my_module_m26.
# print(my_add(5, 10))  # 15
# my_new_obj = MyClass("Carol")
# print(my_new_obj.greet())  # Hello, Carol!

# there is a downside to this approach - we lose the namespace

# now we can also create new alias for the imported function or class
from my_module_m26 import my_add as add, MyClass as MC # this will import only the my_add function from my_module_m26.py file
# again this can be dangerous if we overwite the existing function or class name
print(add(5, 10))  # 15
my_new_obj = MC("Dave")
print(my_new_obj.greet())  # Hello, Dave!

# last way of importing is to import everything from the module
# from my_module_m26 import * # this will import everything from my_module_m26.py file
# this dumps everything into the current namespace - bad practice
# AVOID THIS APPROACH - IT IS NOT RECOMMENDED
# because it can lead to naming conflicts and makes it hard to determine where a name came from.

# so let's import modules from package my_package_m26
# let's import my_classes.py and my_math.py from my_package_m26

# so we need to specify the package name and the module name
from my_package_m26.my_classes import Dog, Cat # this will import only the Dog and Cat classes from my_classes.py file
sparkie = Dog("Sparkie")
sparkie.speak()  # Sparkie barks
whiskers = Cat("Whiskers")
whiskers.speak()  # Whiskers meows

# I could have imported the whole module and used it like this
from my_package_m26 import my_math # this will import the whole my_math module from my_package_m26 package
# now i can use it to add and subtract numbers
print(my_math.my_add(5, 10))  # 15
print(my_math.my_subtract(10, 5))  # 5

# you are allowed to have package with package with same name as module

# let me show you some examples of built-in modules
# let's import the random module from standard library
import random # this is a built-in module that implements pseudo-random number generators for various distributions.
# this module is used to generate random numbers and perform random operations.
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))  # this will print a random element from the list
random.shuffle(my_list) # this will shuffle the list in place
print(my_list)  # this will print the shuffled list

# let me show you a cool way of creating Cartesean product of list and characters

letters = "ABC"
numbers = [1,2]
# i want to generate a list of tuples with all combinations of letters and numbers
# this is a cartesian product of letters and numbers

from itertools import product # this is a built-in module that provides functions that create iterators for efficient looping.
# this module is used to create iterators for efficient looping.
# now let's use it
cartesian_product = list(product(letters, numbers)) # this will create a cartesian product of letters and numbers
print(cartesian_product)  # this will print the cartesian product of letters and numbers
# if I did not know about this standar library module, I would have to write a nested loop to create the cartesian product of letters and numbers
also_cartesian_product = []
for letter in letters:
    for number in numbers:
        also_cartesian_product.append((letter, number))
print(also_cartesian_product)  # this will print the cartesian product of letters and numbers

# full list of standard library modules can be found here
# https://docs.python.org/3/library/index.html
# this is a good resource to find out what modules are available in standard library

# so use modules in your current folder to organize your code
# if you have a lot of code, it is better to split it into multiple files and use modules to organize your code\
# for truly large project you can use packages (sub-directories) to organize your code