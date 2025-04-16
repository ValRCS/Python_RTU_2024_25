# So we already know about lists and how to work with them.
# why would we need another data structure like a dictionary?
# lists work great when we have something in specific order
# but what if we want to store data that is not in a specific order?
# we still want fast access, deletion and insertion of data
# dictionaries are the answer to that problem

# dictionaries offer us a collection of key-value pairs
# Latviski: atslēgu-vērtību pāri
# they are unordered(actually order of insertion is preserved since Python 3.6), mutable and indexed
# they are also iterable, so we can loop through them

# other programming languages call dictionaries by different names:
# hash maps, associative arrays, maps, etc.

# the main idea is to "instantly" find the value by its key
# so we can use any immutable data type as a key
# this instantly means that we can access the value in O(1) time complexity - constant time
# this works even on very large data sets

# some properties of dictionaries in Python:
# 1. they are mutable - we can change them after creation
# 2. they are unordered - actually order of insertion is preserved since Python 3.6
# 3. they are indexed - we can access values by their keys
# 4. these keys are unique - we can't have two same keys in a dictionary
# 5. they can store any data type as a value - even other dictionaries
# 6. keys can be any immutable data type - strings, numbers, tuples, etc. - requirement is that they hash
# 7. dictionaries are iterable - we can loop through them
# 8. they can be nested - we can have dictionaries inside dictionaries

# so let's create an empty dictionary
empty_dict = {}
print(empty_dict)  # prints {}
# how many items in the dictionary?
print(f"Number of items in the dictionary: {len(empty_dict)}")  # prints 0

# let's create a dictionary with some data
# let's create a phone book
tel_dict = {
    "John": 123456789,
    "Jane": 987654321,
    "Bob": 555555555,
    "Alice": 111111111
}

# print our dictionary
print(tel_dict)  # prints {'John': 123456789, 'Jane': 987654321, 'Bob': 555555555, 'Alice': 111111111}
# how many items in the dictionary?
print(f"Number of items in the dictionary: {len(tel_dict)}")  # prints 4

# so main idea is that I can get Alice's phone number quickly
# let's get Alice's phone number
print(f"Alice's phone number: {tel_dict['Alice']}")  # prints Alice's phone number: 111111111

# compare it with 2d list of persons and their numbers
# let's create a 2d list with some data
phone_list = [
    ["John", 123456789],
    ["Jane", 987654321],
    ["Bob", 555555555],
    ["Alice", 111111111]
]

# to find Alice's phone number we have to loop through the list
# let's find Alice's phone number
for person in phone_list:
    if person[0] == "Alice":
        print(f"Alice's phone number: {person[1]}")  # prints Alice's phone number: 111111111
        break  # we found Alice, so we can stop searching
# this is O(n) time complexity - linear time

# let's add Valdis phone number
# to the dictionary
# to add we simply assign a value to a key
tel_dict["Valdis"] = 28888318 

# let's print the dictionary again
print(tel_dict)  # prints {'John': 123456789, 'Jane': 987654321, 'Bob': 555555555, 'Alice': 111111111, 'Valdis': 28888318}
# how many items in the dictionary?
print(f"Number of items in the dictionary: {len(tel_dict)}")  # prints 5

# addition of key-value pair is O(1) time complexity - constant time

# how about removing John from the dictionary?
# to remove we use the del keyword - this is O(1) time complexity - constant time

del tel_dict["John"]
# let's print the dictionary again
print(tel_dict)  # prints {'Jane': 987654321, 'Bob': 555555555, 'Alice': 111111111, 'Valdis': 28888318}
# how many items in the dictionary?
print(f"Number of items in the dictionary: {len(tel_dict)}")  # prints 4

# let's try deleting a key that doesn't exist
try:
    del tel_dict["John"]
except KeyError:
    print("Key not found")  # prints Key not found

# how about checking whether some key exists - this is very quick
# very common is to check if some key exists in the dictionary
if "Bob" in tel_dict:
    print(f"Bob's phone number: {tel_dict['Bob']}")  # prints Bob's phone number: 555555555
else:
    print("Bob not found")
# this is O(1) time complexity - constant time

# instead of checking using in we can use get method
# this is also O(1) time complexity - constant time
print("Bob's phone number", tel_dict.get("Bob"))  # prints Bob's phone number 555555555
# let's check if Voldemort is in the phone book
print("Voldemort's phone number", tel_dict.get("Voldemort"))  # prints Voldemort's phone number None
# we could supply custom default value to the get method
# this is also O(1) time complexity - constant time
print("Voldemort's phone number", tel_dict.get("Voldemort", "Not found"))  # prints Voldemort's phone number Not found

# we can of course use variables for keys and values
key = "Carol"  # key is just a name for variable could be anything else valid for variable name
value = 123456789 # same thing for variable called value could be any valid variable name
# let's add Carol's phone number
tel_dict[key] = value
# let's print the dictionary again
print(tel_dict)  # prints {'Jane': 987654321, 'Bob': 555555555, 'Alice': 111111111, 'Valdis': 28888318, 'Carol': 123456789}

# now I can get the value by key
print(f"{key}'s phone number: {tel_dict[key]}")  # prints Carol's phone number: 123456789

# how about looping through the dictionary?
# we have a couple of ways
# 1. loop through the keys - this is O(n) time complexity - linear time
# 2. loop through the values - this is O(n) time complexity - linear time
# 3. loop through the key-value pairs - this is O(n) time complexity - linear time

# let's go through keys
for key in tel_dict: # we could have also used tel_dict.keys() - same thing
    print(f"KEY {key}: PHONE {tel_dict[key]}")  # prints Jane: 987654321, Bob: 555555555, Alice: 111111111, Valdis: 28888318, Carol: 123456789
    # note no need to use get method here because we KNOW that key exists in the dictionary

# another way is to get both
# key and value at the same time using items() method
# this is O(n) time complexity - linear time
for key, value in tel_dict.items():
    print(f"KEY {key}: PHONE {value} == {tel_dict[key]}")  # prints Jane: 987654321, Bob: 555555555, Alice: 111111111, Valdis: 28888318, Carol: 123456789

# import to note that if we plan to modify keys for dictionary (delete or add) we should use copy of the dictionary
# otherwise we might get unexpected results

# let's create a dictionary of Latvian cities and their populations
latvian_cities = {
    "Rīga": 1000000,
    "Daugavpils": 82000,
    "Liepaja": 82000,
    "Jelgava": 55000,
    "Rīga": 700000, # this will overwrite the previous value
    "Jurmala": 50000,
    "Ventspils": 35000,
    "Rīga": 632_614, # this will overwrite the previous value
}
# in above case keys have to be unique , no error but last key value pair will be preserved
print(latvian_cities)  # prints {'Rīga': 632614, 'Daugavpils': 82000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000}

# so if I decide to overwrite Daugavpils population there is no error
# but I will lose the previous value
latvian_cities["Daugavpils"] = 97_000 # will overwrite if it exists

#if I do not want to overwrite I could check if key exists
if "Daugavpils" in latvian_cities:
    print("Daugavpils already exists")
else:
    latvian_cities["Daugavpils"] = 98_000
print(latvian_cities)

# instead we could use setdefault method
# this will set the value only if key does not exist
# this is O(1) time complexity - constant time
# so let's add Tukums
# this will set the value only if key does not exist
latvian_cities.setdefault("Tukums", 20000)
# let's print the dictionary again
print(latvian_cities)  # prints {'Rīga': 632614, 'Daugavpils': 97000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000, 'Tukums': 20000}
# now if I try with setdefault again it will not change the value
latvian_cities.setdefault("Tukums", 30000) # will NOT change because key already exists
# let's print the dictionary again
print(latvian_cities)  # prints {'Rīga': 632614, 'Daugavpils': 97000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000, 'Tukums': 20000}

# so let's create a new dictionary of cities under 60000
small_cities = {}
# let's loop through the latvian_cities dictionary and add cities under 60000 to the small_cities dictionary
for city_name, population in latvian_cities.items():
    if population < 60000:
        small_cities[city_name] = population

# above could have been done with dictionary comprehension
also_small_cities = {k: v for k, v in latvian_cities.items() if v < 60000}

# just like with lists we use dictionary comprehension for simple cases
# for more complicated cases we use loops like above

# now let's see difference between alias and copy

latvian_cities_alias = latvian_cities # just like with lists NOT a copy of the dictionary
latvian_cities_backup = latvian_cities.copy() # this is a copy of the dictionary

# let's go through original latvian_cities and delete small cities under 60000
# this is O(n) time complexity - linear time
for city_name, population in latvian_cities.copy().items():
    if population < 60000:
        del latvian_cities[city_name] # this also affects latvian_cities_alias !

# after deletion let's see our dictionaries
print(latvian_cities)  
print(latvian_cities_alias)  
# now our backkup
print("BACKUP", latvian_cities_backup)  

# now I could clear original\
latvian_cities.clear() # this will clear the dictionary
# let's print the dictionary again
print(latvian_cities)  # prints {}
print(latvian_cities_alias)  # prints {}
print(latvian_cities_backup)  # prints {'Rīga': 632614, 'Daugavpils': 97000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000, 'Tukums': 20000}

# now I can just point original to the backup
latvian_cities = latvian_cities_backup # this is just a reference to the backup dictionary
# let's print the dictionary again
print(latvian_cities)  # prints {'Rīga': 632614, 'Daugavpils': 97000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000, 'Tukums': 20000}

# then we have an update method
# this methods add key-value pairs from another dictionary to the current dictionary
# it will overwrite existing keys
mini_cities = {
    "Aizkraukle": 5000,
    "Alūksne": 4000,
    "Balvi": 3000,
    "Bauska": 2000,
    "Cēsis": 1000,
    "Varakļāni": 500,
    "Daugavpils": 1000, # this will overwrite the previous value
}

latvian_cities.update(mini_cities) # this will add all key-value pairs from mini_cities to latvian_cities
# let's print the dictionary again
print(latvian_cities)  # prints {'Rīga': 632614, 'Daugavpils': 1000, 'Liepaja': 82000, 'Jelgava': 55000, 'Jurmala': 50000, 'Ventspils': 35000, 'Tukums': 20000, 'Aizkraukle': 5000, 'Alūksne': 4000, 'Balvi': 3000, 'Bauska': 2000, 'Cēsis': 1000, 'Varakļāni': 500}

# now let's reverse a dictionary
# but first let's filter it to tiny cities less than 5000
tiny_cities = {k: v for k, v in latvian_cities.items() if v < 5000}
# let's print the dictionary again
print(tiny_cities)  # prints 
# now let's make a new reverse dictionary

# reverse_tiny_cities = {v: k for k, v in tiny_cities.items()}
# same us loop
reverse_tiny_cities = {}
for city, pop in tiny_cities.items():
    reverse_tiny_cities[pop] = city # note the reversal of key and value
# let's print the new dictionary
print(reverse_tiny_cities) 
# now I can look up city by population
# so which city has population 3000
print(f"City with population 3000: {reverse_tiny_cities[3000]}")  # prints City with population 3000: Balvi

# one downside with this reversal we lost some data
# so if we have two or more cities with same population we will lose one of them
# instead we could use a list of cities with same population
# so let's create a new dictionary with list of cities with same population

new_tiny_cities_by_pop = {}
# let's loop through the tiny_cities dictionary and add cities to the new dictionary
# this is O(n) time complexity - linear time
for city, pop in tiny_cities.items():
    if pop not in new_tiny_cities_by_pop: # so i look if my new diction is using value from old dict
        new_tiny_cities_by_pop[pop] = [city] # create a list with first city
    else:
        new_tiny_cities_by_pop[pop].append(city) # add city to the value which is a list

# let's print the new dictionary
print(new_tiny_cities_by_pop)  

# typical use of dictionaries is in conjuction with lists

# this translates well to retrieval from various databases where keys are column names
# let's have a list of dictionaries that represents Latvian beers with their names, prices and alcohol content as keys

latvian_beers = [
    {"name": "Aldaris", "price": 1.5, "alcohol": 5.0},
    {"name": "Cēsu", "price": 1.2, "alcohol": 4.5},
    {"name": "Lāčplēsis", "price": 1.8, "alcohol": 6.0},
    {"name": "Rīgas", "price": 1.3, "alcohol": 5.2},
    {"name": "Valmiermuiža", "price": 2.0, "alcohol": 4.8},
    {"name": "Tērvetes", "price": 1.6, "alcohol": 5.5},
    {"name": "Zelta", "price": 1.4, "alcohol": 4.7},
    {"name": "Bauskas", "price": 1.7, "alcohol": 5.3},
]

# i use * to unroll the list of dictionaries and then print them one by one
print(*latvian_beers, sep="\n")  # prints the list of dictionaries

# now let's sort them by price in ascending order
# to do so I will pass key to the sorted function
sorted_by_price = sorted(latvian_beers, key=lambda beer: beer["price"])
# let's print the sorted list
print("Sorted by price:")
for beer in sorted_by_price:
    print(f"{beer['name']}: {beer['price']} EUR, {beer['alcohol']}%")  # prints the sorted list of beers by price


