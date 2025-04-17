# we know two compound(complex) data types in python - 
# list and dictionary.
# but actually we have another compound data type - tuple that we have used a bit already

# tuple is very similar to list but with one key difference -
# tuple is immutable - it cannot be changed in size once created

# Latvian name for tuples is "kortežs" - thank you LZA Termini
# https://termini.gov.lv/atrast/tuple

# Philosophy of tuples vs lists:
# - tuples are for heterogeneous data - different types of data - typically smaller data
# - lists are for homogeneous data - same type of data could be larger data
# - tuples are for data that doesn't change

my_tuple = (1, 2, 3, 4, 5) # we use regular brackets () for tuples
print(my_tuple) # (1, 2, 3, 4, 5)
# more interesting we do not need parentheses at all - we can just use commas to create a tuple
also_my_tuple = 5, 6, 7, 8, 9 # this is a tuple too - but it is not a list - it is a tuple
print(also_my_tuple) # (5, 6, 7, 8, 9)

# so in our functions to return multiple values we used tuples

# let's recreate a function that retuns min, avg and max of a list of numbers
def min_avg_max(numbers):
    """
    Function to calculate min, avg and max of a list of numbers
    """
    if len(numbers) == 0:
        return None, None, None # we return a tuple with three values - None, None, None
    else:
        min_num = min(numbers)
        max_num = max(numbers)
        avg_num = sum(numbers) / len(numbers)
        return min_num, avg_num, max_num # we return a tuple with three values - min, avg and max
    
# let's test our function
number_list = [1, 2, 3, 4, 5]
min_num, avg_num, max_num = min_avg_max(number_list) # I unpack the tuple into three variables - min_num, avg_num and max_num
print(f"Min: {min_num}, Avg: {avg_num}, Max: {max_num}") # Min: 1, Avg: 3.0, Max: 5

# i could have just returned a tuple without breakign it down
my_result_tuple = min_avg_max(number_list)
print(my_result_tuple) # (1, 3.0, 5)
# then I could use index to access
# the values of the tuple - but it is not very readable
print(my_result_tuple[0]) # 1 - min
print(my_result_tuple[1]) # 3.0 - avg
print(my_result_tuple[2]) # 5 - max
# also slicing would work on tuples

# instead I unpacked the tuple into three variables - min_num, avg_num and max_num
# so we use unpacking to get the values of the tuple into separate variables

# in fact I can use both unpacking and packing at same time to swap values
good_year = 2024
bad_year = 2025
print(good_year) # 2024
print(bad_year) # 2025

# so we can swap values of two variables using tuple unpacking
good_year, bad_year = bad_year, good_year # this is tuple unpacking - we create a tuple with two values and unpack it into two variables
# this works by packing tuple on right side first
# then immediately unpacking it into two variables on left side
print(good_year) # 2025
print(bad_year) # 2024

# if I did not know about the above trick I would have to use a temporary variable to swap values

# let's go back to dictionaries and their use of tuples
# first about items() method - it returns a list of tuples - each tuple is a key-value pair

# let's make a small dictionary
my_dict = {
    "name": "Valdis",
    "age": 50,
    "city": "Rīga",
    "profession": "programmer",
}
# let's use items() method to get a list of tuples - each tuple is a key-value pair
print(my_dict.items()) # dict_items([('name', 'Valdis'), ('age', 50), ('city', 'Rīga')])
# it looks like list of tuples but not exactly - it is a special type of object - dict_items

# I can convert this to actual list of tuples
my_tuple_list = list(my_dict.items()) # I convert dict_items to list of tuples
print(my_tuple_list) #

# i can pass this list of tuples back to dict() and get a new dictionary
new_dict = dict(my_tuple_list) # I convert list of tuples to dictionary 
print(new_dict) # {'name': 'Valdis', 'age': 50, 'city': 'Rīga', 'profession': 'programmer'}
# so we can convert between dictionaries and lists of tuples

# another use of tuples is as keys in dictionaries
# so let's create an employees dictionary
# keys will be tuples of (name, surname) and values will inner dictionary with age and profession and hobby

employees = {
    ("Valdis", "Bergs"): {
        "age": 50,
        "profession": "programmer",
        "hobby": "fishing",
    },
    ("Jānis", "Bērziņš"): {
        "age": 30,
        "profession": "teacher",
        "hobby": "reading",
    },
    ("Jānis", "Krūmiņš"): {
        "age": 35,
        "profession": "doctor",
        "hobby": "running",
    },
    ("Anna", "Ozola"): {
        "age": 25,
        "profession": "doctor",
        "hobby": "running",
    },
}
# let's print the dictionary
print(employees) # {('Valdis', 'Bergs'): {'age': 50, 'profession': 'programmer', 'hobby': 'fishing'}, ('Jānis', 'Bērziņš'): {'age': 30, 'profession': 'teacher', 'hobby': 'reading'}, ('Jānis', 'Krūmiņš'): {'age': 35, 'profession': 'doctor', 'hobby': 'running'}, ('Anna', 'Ozola'): {'age': 25, 'profession': 'doctor', 'hobby': 'running'}}

# how to get ('Anna', 'Ozola') hobby
print(employees[("Anna", "Ozola")]["hobby"]) # running
# it works because first [('Anna', 'Ozola')] get value of the key - which is a dictionary
# then I get the value of the key "hobby" from the dictionary

# how about printing only Jānis info
# I can use a loop to iterate over the keys of the dictionary
for key, value in employees.items(): # this is a tuple unpacking - key is a tuple and value is a dictionary
    if key[0] == "Jānis": # I check if first name is Jānis
        # i just have to know that 0 is name and 1 is surname
        print(key, value) # I print the key and value - which is a tuple and a dictionary
        # here I could add this to another dictionary or do something else
        # make email , send report etc etc

# last on tuple methods
# there are only two
# count() - counts the number of occurrences of a value in the tuple
# index() - returns the index of the first occurrence of a value in the tuple
simple_tuple = 3,6,7,7,9,3,3,3
print("How many 3?", simple_tuple.count(3)) # 4 - it counts the number of occurrences of 3 in the tuple
# how about first index of 7?
print("First index of 7?", simple_tuple.index(7)) # 2 - it returns the index of the first occurrence of 7 in the tuple
# since tuples are immutable they lack the list mutation methods - append, insert, remove, pop, clear, sort, reverse