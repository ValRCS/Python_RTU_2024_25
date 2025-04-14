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
go_eat_multiple(restaurant_list, food_list)

# should be really full
print("Should be really full")
