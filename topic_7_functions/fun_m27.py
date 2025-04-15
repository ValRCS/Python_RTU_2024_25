# As our programs / code grow more complex, 
# we need to break them down into smaller, more manageable pieces.
# Functions are a way to do this.
#  Functions allow us to group related code together and give it a name.

# Functions are reusable pieces of code that can be called multiple times throughout a program.
# They can take inputs (called parameters or arguments) and return outputs (called return values).
# Functions can also be defined to not take any inputs or return any outputs.

# Functions let us abstract away the details of how something is done, so we can focus on what we want to do.
# This makes our code easier to read and understand.

# Ideal function does one thing and does it well.
# It should be small enough to be easily understood and tested.

# In real life you end up with functions that do more than one thing.
# This is not a problem as long as the function is still easy to understand and test.

# functions let us avoid repeating code. - DRY principle
# DRY = Don't Repeat Yourself
# If you find yourself copying and pasting code, it's a sign that you should create a function.
# there are of course exceptions to this rule, but in general, if you find yourself copying and pasting code, it's a sign that you should create a function.
# Functions can also help us avoid bugs. If we have a piece of code that is used in multiple places, and we need to change it, we only have to change it in one place.

# Good function names are descriptive and indicate what the function does.
# Avoid using vague names like "do_something" or "function1".

# Let's look at what would lead us to create a function.
# we want to go eat lunch, but we need to do a few things first:
# 1. wash hands
# 2. make sandwich
# 3. eat sandwich
# 4. wash hands again

# I will emulate this with print
# print("Washing hands")
# print("Making sandwich")
# print("Eating sandwich")
# print("Washing hands again")
# This is a lot of repeated code.
# to avoid copy and pasting the same code over and over again, we can create a function.
# Let's create a function that does all of this for us.


def eat_lunch(): # again we use : to indicate that this is a function definition so indent the next lines
    # inner scope of function
    print("Washing hands")
    print("Making sandwich")
    print("Eating sandwich")
    # let's drink kefir
    print("Drinking kefir")
    print("Washing hands again")
# function definition ends here

# eat_lunch() # this is a function call, we are calling the function we just defined

# # i could eat lunch 3 times 
# print("Let's eat lunch 3 times")
# for _ in range(3): # _ is just a variable but we are saying we do not care about it
#     eat_lunch() # this is a function call, we are calling the function we just defined

# let's make a function make and eat something
def make_and_eat(something): # we are passing a parameter to the function, this is called an argument
    print(f"Making {something}")
    print(f"Eating {something}")

print("Thinking of eating something.... 🤔")

# let's make kebab and eat it
make_and_eat("kebab") # this is a function call, we are calling the function we just defined

# lunch_choice = input("What do you want to eat for lunch? ") # we are passing a parameter to the function, this is called an argument
lunch_food = "poke bowl" # we are passing a parameter to the function, this is called an argument
make_and_eat(lunch_food) # this is a function call, we are calling the function we just defined

# print("Should be full hopefully")

# how about drinking something as a parameter
def drink(beverage): # we are passing a parameter to the function, this is called an argument
    print(f"Drinking {beverage}")
    print(f"Drinking {beverage} again")

drink("water") # this is a function call, we are calling the function we just defined
drink("kefir") # this is a function call, we are calling the function we just defined

# now let's make a function called eat and drink that takes two parameters
def eat_and_drink(entree, liquid): # we are passing a parameter to the function, this is called an argument
    # entree and liquid variables are available only in this scope
    # they are not available outside of this function
    # this is called local scope
    print(f"Will eat {entree} and drink {liquid}")
    # now I will actually call the functions we defined before
    make_and_eat(entree) # this is a function call, we are calling the function we just defined
    drink(liquid) # this is a function call, we are calling the function we just defined
    print(f"Done eating {entree} and drinking {liquid}")

# let's call the function with two parameters
eat_and_drink("pizza", "juice") # this is a function call, we are calling the function we just defined

# now let's make a function that eats and drinks lots of things from lists
def eat_and_drink_multiples(entrees, liquids): # we are passing a parameter to the function, this is called an argument
    # entree and liquid variables are available only in this scope
    # they are not available outside of this function
    # this is called local scope
    print(f"Will eat {entrees} and drink {liquids}")
    # I want to call eat and drink
    # for nested lists
    for entree in entrees: # this is a for loop, we are iterating over the list of entrees
        for liquid in liquids: # this is a for loop, we are iterating over the list of liquids
            eat_and_drink(entree, liquid)
    print("Done eating and drinking")

food_list = ["pizza", "kebab", "sushi"]
drink_list = ["water", "green tea"]

# let's call the function with two parameters
# eat_and_drink_multiples(food_list, drink_list) # this is a function call, we are calling the function we just defined
# print("Should be full hopefully")

# let's make a function that prints addition of two numbers
def print_add(a, b):
    result = a + b # this is a local variable, it is only available in this function
    print(f"The result of {a} + {b} is {result}")
    # in Python functions return None by default

print_add(5,9) # this is a function call, we are calling the function we just defined

# in the above print_add function we are not returning anything!
# we have no easy way of storing the result of the addition

# instead let's make an add function
def add(a, b):
    result = a + b # this is a local variable, it is only available in this function
    # i could do more stuff here including adjusting result..
    return result # we are returning the result of the addition
# this is called a return value

print(add(7,3)) # this is a function call, we are calling the function we just defined

# I could immediately return something
# let's make multiply function
def multiply(a, b):
    return a * b # we are returning the result of the multiplication
# this is called a return value

not_result = print_add(10,5)
print(f"This is not a result: {not_result}") # this will print None because print_add does not return anything

# but we can use the result of the multiply function and add function as well
add_result = add(7,3)
multiply_result = multiply(7,3)
print(f"Add result: {add_result}")
print(f"Multiply result: {multiply_result}")

# now I gain ability to compose functions within function

add_multiply_result = add(multiply(10,8), add(5,2))
print(f"Add multiply result: {add_multiply_result}")

# how about returning multiple values
# we simply use , to separate the values we want to return
def min_and_max(sequence):
    my_min = min(sequence) # this is a built in function that returns the minimum value of a sequence
    my_max = max(sequence) # this is a built in function that returns the maximum value of a sequence
    return my_min, my_max # we are returning the minimum and maximum values of the sequence

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_min, my_max = min_and_max(my_numbers) # we are unpacking the values returned by the function

print(f"Min: {my_min}, Max: {my_max}") # this will print the minimum and maximum values of the sequence

# how about a function that takes start number and end number
# and returns a list of cubes from that start and end INCLUSIVE
# let's make a function that takes start number and end number
def cubes(start, end):
    # this is a list comprehension that creates a list of cubes from start to end
    # return [i**3 for i in range(start, end+1)] # we are returning the list of cubes
    # I could do it the old fashioned way as well
    cubes_list = [] # this is an empty list that will hold the cubes
    for i in range(start, end+1): # this is a for loop that iterates from start to end
        cubes_list.append(i**3) # this is a list that holds the cubes
    return cubes_list # we are returning the list of cubes

my_cubes = cubes(1, 10) # we are calling the function we just defined
print(f"Cubes from 1 to 10: {my_cubes}") # this will print the list of cubes from 1 to 10

# we might want to indicate what data types we want to use
# so let's create add with types
def add_with_types(a: int, b: int) -> int: # this is a function that takes two integers and returns an integer
    """ This function takes two integers and returns their sum. \n
    Inputs:\n
    a: int - first integer\n
    b: int - second integer\n
    Outputs:\n
    int - sum of the two integers
    """
    # above is a docstring, this is a string that describes what the function does
    # it is optional but it is a good practice to include it
    # it is not a type hint, it is a docstring
    # docstrings are used to build documentation for the function
    # also can be used to write books, publish websites, etc.
    return a + b # we are returning the result of the addition

my_int = add_with_types(5, 10) # this is a function call, we are calling the function we just defined
print(f"Add with types: {my_int}") # this will print the result of the addition

# how about floats?
my_float = add_with_types(5.5, 10.5) # this is a function call, we are calling the function we just defined
print(f"Add with types: {my_float}") # this will print the result of the addition

# how about strings
my_string = add_with_types("Valdis ", "vakariņas")
print(f"Add with types: {my_string}") # this will print the result of the addition

# now let's talk about default values
# Python lets us be lazy and use default values in function

# let's make lazy power function that takes two parameters
# base and exponent
# by default exponent will be 2 - square
def lazy_power(base: float, exponent: int = 2, verbose = False) -> float: # this is a function that takes two parameters and returns a float
    """ This function takes a base and an exponent and returns the base raised to the exponent. \n
    Inputs:\n
    base: float - base number\n
    exponent: int - exponent number\n
    verbose: bool - if True, print the result\n
    Outputs:\n
    float - base raised to the exponent
    """
    result = base ** exponent # this is the power operation
    if verbose:
        print(f"Base: {base}, Exponent: {exponent}, Result: {result}")
    # we could do more stuff here including adjusting result..
    # note result is just a name for local variable - could be any valid name
    return result # we are returning the result of the power operation

# so squares only need one parameter
print(lazy_power(10))
# now if I want something else then I pass second parameter
print(lazy_power(2, 8)) # this is a function call, we are calling the function we just defined
# how about square root of 4?>
print(lazy_power(4, 0.5)) # this is a function call, we are calling the function we just defined

# philosophically our defaults should be "sane" - meaning values more commonly used
# but this is not a rule - just a suggestion

# now I can use verbose Flag 
# to indicate if I want to print the result or not
print(lazy_power(10, 3, True)) # this is a function call, we are calling the function we just defined

# it is recommended that you call boolean arguments explicitly by keyword
# so that it is clear what you are passing to the function
print(lazy_power(10, 3, verbose=True)) # this is a function call, we are calling the function we just defined
# I could mix and match all 3 arguments using keywords but it is not recommended
print(lazy_power(verbose=True, base=10, exponent=3)) # this is a function call, we are calling the function we just defined
# above mixing of orders is to be avoided but it is possible

# let's make a f unction that produces a product from variable number of arguments
# this is called variable length arguments
def product_var(*args): # this is a function that takes variable number of arguments
    """ This function takes a variable number of arguments and returns the product of the arguments. \n
    Inputs:\n
    *args: variable number of arguments\n
    Outputs:\n
    result - product of the arguments
    """
    print(f"Got {len(args)} arguments") # this will print the number of arguments passed to the function
    result = 1 # this is the initial value of the product
    for arg in args: # this is a for loop that iterates over the arguments
        result *= arg # this is the product operation
    return result # we are returning the product of the arguments

my_product = product_var(1, 2, 3, 4, 5) # this is a function call, we are calling the function we just defined
print(f"Product of 1, 2, 3, 4, 5: {my_product}") # this will print the product of the arguments

# still *args might not be best here, we could have used just a list
# so let's define product_from_list
def product_from_list(numbers: list) -> float:
    """ This function takes a list of numbers and returns the product of the numbers. \n
    Inputs:\n
    numbers: list - list of numbers\n
    Outputs:\n
    result - product of the numbers
    """
    result = 1 # this is the initial value of the product
    for number in numbers: # this is a for loop that iterates over the arguments
        result *= number # this is the product operation
    return result # we are returning the product of the arguments

# so the difference here is not in the code inside but how we pass values to this product function
my_list = [1, 2, 3, 4, 5] # this is a list of numbers
my_product = product_from_list(my_list) # this is a function call, we are calling the function we just defined
print(f"Product of {my_list}: {my_product}") # this will print the product of the arguments

# i could call directly using list
also_product = product_from_list([10, 1, 2, 3]) # this is a function call, we are calling the function we just defined
print(f"Product of [10, 1, 2, 3]: {also_product}") # this will print the product of the arguments