# Python has another data type that is similar to a list called a tuple.
# In Latvian tuple is called "korteža" or "kortežs"
# A tuple is a collection which is ordered and unchangeable.
# Typically we use tuples to pass around a collection of values 
# that are related to each other.
# however those values might have different data types

# Philisophically, lists should have similar data types, - homogeneous
# Tuples can have different data types - heterogeneous

# Tuples are defined by using parentheses () instead of square brackets []
# Tuples are immutable, meaning they cannot be changed after creation

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# in fact we do not even need parentheses
also_tuple = 3,5,9 
print(also_tuple)

# so now you can see how tuples are used to return multiple values from a function
# let's create a function that returns two values
def get_min_max(numbers):
    return min(numbers), max(numbers) # returns tuple of size 2

my_min_max_tuple = get_min_max([1, 2, 3, 4, 5])
print(my_min_max_tuple)

# same things as list indexes and slices apply to tuples
# but tuples are immutable, so we cannot change them
# first item of tuple
print(my_min_max_tuple[0])
# second item of tuple
print(my_min_max_tuple[1]) # or -1 here would be same

# so tuples have NO IN PLACE methods
# but we can convert them to a list and back to a tuple
# let's convert tuple to list
my_list = list(my_min_max_tuple)
print(my_list)
# let's change the first element of the list
my_list[0] = 100
print(my_list)
# let's convert list back to tuple
my_min_max_tuple = tuple(my_list)
print(my_min_max_tuple)

# also dictionaries items return something that converts to a list of tuples
# let's create a dictionary
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
# let's get the items of the dictionary
my_items = my_dict.items()
print(my_items)
# i can convert this to list
my_items_list = list(my_items)
print(my_items_list)

# now you can see what happens when we loop through dictionary items
for key, value in my_items: 
    print(f"{key}: {value}")
# this works because inner tupples are all size 2

# this is called tuple unpacking
# let's print my_min_max_tuple again
print(my_min_max_tuple)
# let's unpack it into two variables
min_value, max_value = my_min_max_tuple
print(f"min: {min_value}, max: {max_value}")

# this unpacking can be used to swap values efficiently

year_a, year_b = 2024, 2025
print(f"year_a: {year_a}, year_b: {year_b}")

# now I can swap them in one line - Pythonic way
year_a, year_b = year_b, year_a # first I make tuple on the right side
# then I unpack it to the left side
print(f"year_a: {year_a}, year_b: {year_b}")

# in other languages without support for unpacking
# we would need a temporary variable to swap values
# let's say I want to swap values of two variables
# let's create a temporary variable
temp = year_a
# now I can swap values
year_a = year_b
year_b = temp
# now let's print them again
print(f"year_a: {year_a}, year_b: {year_b}")

# so there are only two tuple methods
# count() and index()
# let's see what they do
# let's create a tuple with some duplicate values
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_tuple)
# print count of 3
print(my_tuple.count(3)) # 2 appears twice
# how about index of 5 ?
print(f"first index of 5: {my_tuple.index(5)}") # 5 appears at index 9

# regular slicing works on tuples too
tuple_slice = my_tuple[1:5] # creates new tuple
print(tuple_slice) # (2, 3, 4, 5)

# also tuples could be used as Keys if all values inside are fixed


# typical example would be to use name and last name in tuple
# as key in dictionary
# let's create a dictionary that has tuples as keys
# and professions as values
employees = {
    ('John', 'Doe'): 'Engineer',
    ('Jane', 'Smith'): 'Manager',
    ('Alice', 'Johnson'): 'Designer',\
    ('Valdis', 'Saulespurēns'): 'Programmer',
    ('Valdis', 'Dombrovskis'): 'Programmer', # ! :)
    ('Valdis', 'Zatlers'): 'Doctor',
    ('Valdis', 'Birkavs'): 'Politician',
    ('Valdis', 'Makarovs'): 'Artist',
    ('Valdis', 'Lazdins'): 'Teacher',
    ('Valdis', 'Kozlovskis'): 'Police',

}

# print dictionary
print(employees)

# let's print Valdis Zatlers profession
print(employees[('Valdis', 'Zatlers')]) # Doctor

# so how would I get a new dictionary that only contains person by first name Valdis?

valdis_only = {}
for key, value in employees.items():
    # if we are not sure if key is tuple
    # we can check first and continue if not
    if not isinstance(key, tuple): # isinstance checks if key is tuple
        continue

    if key[0] == 'Valdis': # we have to KNOW that key is a tuple with at least 2 items
        valdis_only[key] = value
print(valdis_only)

# i could make this slightly more readable
# by unpacking key as name, surname

again_valdis_only = {}
# with this approach I gain some clarity
# but I lose protection against non tuple keys or different size tuples
# so I have to be careful here
for (name, surname), value in employees.items():
    if name == 'Valdis':
        again_valdis_only[(name, surname)] = value
print(again_valdis_only)

# again tuples can used as keys in dictionaries
# but lists cannot be used as keys in dictionaries
# because lists are mutable and tuples are immutable

# to be precise tuple values have to be immutable
# and tuple itself has to be hashable

# last thing let's make a list of tuples 
# now Let's food and price
# let's create a list of tuples
food_prices = [
    ('apple', 1.2),
    ('banana', 0.5),
    ('orange', 0.8),
    ('grape', 2.5),
    ('watermelon', 3.0)
]

print(food_prices)

# if I have a list (or tuple) of tuples(or lists) of size 2
# then I can pass this to dict constructor
# and it will create a dictionary from it

price_dict = dict(food_prices)
print(price_dict)

# so I gain advantage that I can look up instantly price of say "watermelon"
print(f"price of watermelon: {price_dict['watermelon']}")



