# As our code grows in complexity, we will need to break it down into smaller, more manageable pieces.
# Functions are a way to do this.

# Functions are reusable pieces of code that can be called from anywhere in your program.

# With functions we abstract away the details of how something is done, and just focus on what it does.
# This allows us to write cleaner, more readable code.

# ideal function does one thing and does it well.
# This is called the Single Responsibility Principle (SRP).

# In real life of course functions can do more than one thing, but we should try to keep them as simple as possible.
# This is called the DRY principle (Don't Repeat Yourself).

# Let's say I want to go eat and order food. 
# I will emulate this with print statements.

# print("Go to the restaurant")
# print("Look at the menu")
# print("Order food")
# print("Wait for food")
# if I want to eat again, I have to repeat all these steps.
# so without my own functions I'd have to copy and paste the same code over and over again.
# This is not DRY and not very readable.

# in Python we named our functions using snake_case.
# Alternatively we could use camelCase, but this is not the convention in Python.
# what you should not do is mix both styles.

# typicall functions are verbs, because they do something.
# but this is not a hard rule.

# let's create our walk to restaurant function.
def walk_into_restaurant():
    print("Go to the restaurant")
    print("Open door")
    print("Walk to table") # we could add if check here for waiting list
    print("Sit down")

# so function needs to be called to work
# walk_into_restaurant()
# this is called a function call.
# i can call it again

# we can utilize an existing function into our function
# that includes previously defined functions of our own or built-in functions.
# let's create a function that orders food.
def order_food():
    print("Look at the menu")
    print("Order food")
    print("Wait for food")

# now I can combine both
# this is called function composition.
def go_eat():
    walk_into_restaurant()
    order_food()

# let's call go_eat function
# go_eat()

# let's make a function that takes an argument.
# we will use it to order food
def order_food(food):
    print("Look at the menu")
    print(f"Order {food}")
    print("Wait for food")

# let's get a burger
# order_food("burger")

# now let's make a function that goes to some restaurant
def go_to_restaurant(restaurant):
    print(f"Go to {restaurant}")
    print("Open door")
    print("Walk to table") # we could add if check here for waiting list
    print("Sit down")

# let's make a function that takes two arguments
# one for the restaurant and one for the food
def go_eat(diner, cuisine):
    go_to_restaurant(diner)
    order_food(cuisine)

# now let's go to some restaurant and order some food
# go_eat("Ausmenys", "kebabs")

# print("Should be pretty full")

# let's make a function that takes a list of restaurants and a list of foods
# then goes and eats at each restaurant and orders each food
def go_eat_multiple(restaurants, foods):
    print(f"Going to eat at {len(restaurants)} restaurants and order {len(foods)} foods")
    for restaurant in restaurants:
        for food in foods:
            go_eat(restaurant, food)

restaurant_list = ["Ausmenys", "McDonalds", "Burger King"]
food_list = ["kebabs", "burgers", "fries"]

# now let's go to some restaurant and order some food
# go_eat_multiple(restaurant_list, food_list)

# should be really full
# print("Should be really full")

# let's create a function that prints addition of two numbers
def print_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    # crucially result is lost here!

# let's call it
print_add(2, 3)

# instead let's create a an add function that returns result
def add(a, b):
    return a + b

print("Adding 2 + 3 =", add(2, 3))

saved_addition = add(5,8)
print("Saved addition =", saved_addition)

# let's create multiply function
def multiply(a, b):
    result = a * b # result is typical name for internal variable in function
    print(f"{a} * {b} = {result}")
    return result

mult_result = multiply(2, 3)
print("Multiplication result =", mult_result)

# now we can create multiple function calls in single line
big_result = add(multiply(2, 3), multiply(4, 5))
print("Big result =", big_result)

# let's create a function that takes a number list / iterable and returns the average of the numbers
# actually this function is built into math module 
def get_average(numbers):
    total = sum(numbers) # sum is built-in function
    count = len(numbers) # len is built-in function
    avg = total / count # average is sum divided by count
    return avg
    # we could have done this in one line
    # return sum(numbers) / len(numbers)

# this function will work on any iterable like a list, tuple, set, etc.
# let's create a list of numbers
numbers = [1, 2, 3, 4, 5]
my_average = get_average(numbers)
print("Average of numbers =", my_average)

# now can we call this function again?
# we could if there is no naming conflict
also_average = get_average(range(1, 11)) # range is built-in function
print("Average of range(1, 11) =", also_average)

# how about returning multiple values at once?
# we can simply return multiples values separated by commas (technically as a tuple)

def get_min_max(numbers):
    min_value = min(numbers) # min is built-in function
    max_value = max(numbers) # max is built-in function
    return min_value, max_value # return as tuple

my_min, my_max = get_min_max(numbers)
print("Min =", my_min)  
print("Max =", my_max)

# now Python offers so called type hints to help us understand what type of arguments a function takes and what type it returns.

# let's create a function add with type
def add_with_type(a: int, b: int, verbose = False) -> int:
    """	Adds two numbers and returns the result.\n
    a: first number - int\n
    b: second number - int\n\n
    Output:\n
    result: sum of a and b - int
    """
    result = a + b
    if verbose:
        print(f"VERBOSE: {a} + {b} = {result}")
    return result

print(add_with_type(2, 3))
print(add_with_type(2.5, 3.5))
# how about Valdis and Šokolāde?
print(add_with_type("Valdis", " Šokolāde")) 

# now we can use it to debug as well
add_result = add_with_type(2, 3, True)
print("Add result =", add_result)

# even better would be to use named arguments
also_add_result = add_with_type(a=20, b=30, verbose=True)
print("Also add result =", also_add_result)

# now we can use named parameters without worrying about specifying them in order
# this is called keyword arguments.
# let's see this in print function
print("Hello", "Functions",  end=":)!\n", sep=", ")

# let's make a lazy power function by default its power will be 2
def lazy_power(base, exponent=2):
    """Raises base to the power of exponent.
    Input:
    base: base number - int or float
    exponent: exponent number - int or float, default is 2\n\n
    Output:
    result: base raised to the power of exponent - int or float
    """
    result = base ** exponent
    return result

# now we can use it with 1 or two arguments
print("3 to the power of 2 =", lazy_power(3)) # 3^2 = 9
print("3 to the power of 4 =", lazy_power(3, 4)) # 3^3 = 27
print("square root of 9 =", lazy_power(9, 0.5)) # 9^0.5 = 3.0

# finally we have *args and later also **kwargs(in next lecture)

# for now let's look at *args
# with *args we can take unlimited number of arguments
# this is called variable length arguments
# let's make a function called product
def product(*args, verbose=False):
    """Returns the product of all arguments.
    Input:
    args: unlimited number of arguments - int or float\n\n
    Output:
    result: product of all arguments - int or float
    """
    result = 1
    for arg in args: # so i can loop through all arguments
        if verbose:
            print(f"Multiplying {result} * {arg}")
        result *= arg

    if verbose:
        print("Final result =", result)
    return result

# let's test it on some arguments
print("Product of 2, 3, 4 =", product(2, 3, 4)) # 2*3*4 = 24

# now let's debug something
print("Product of 5, 6, 9 with verbose =", product(5, 6, 9, verbose=True)) # 2*3*4 = 24

# alternative to *args would be simply to pass in a list
# let's see how this would work with list_product function
def list_product(numbers, verbose=False):
    """Returns the product of all numbers in a list.
    Input:
    numbers: list of numbers - int or float\n\n
    Output:
    result: product of all numbers - int or float
    """
    result = 1
    for number in numbers:
        if verbose:
            print(f"Multiplying {result} * {number}")
        result *= number

    if verbose:
        print("Final result =", result)
    return result

# the code is essentially the same
# the difference will be in what we call the function with
# let's test it on some arguments
print("Product of [2, 3, 4] =", list_product([2, 3, 4])) # 2*3*4 = 24

# now let's pass in range
print("Product of range(1, 6) =", list_product(range(1, 6), verbose = True)) # 1*2*3*4 = 24

# last thing if there is no return statement in the function, it will return None by default.!
# compare print_add and add functions
print_add_result = print_add(2, 3)
print("Print add result =", print_add_result) # None
print("Print add result type =", type(print_add_result)) # NoneType

add_result = add(2, 3)
print("Add result =", add_result) # 5
print("Add result type =", type(add_result)) # int
# so if you want to return something from a function, you need to use return statement.