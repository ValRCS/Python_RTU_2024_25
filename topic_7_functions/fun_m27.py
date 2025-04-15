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