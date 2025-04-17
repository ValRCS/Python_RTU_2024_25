# we already know list data structure
# we know how to access data in list by index
# lists are great when we know the index of the data we want to access
# if our data is not in order, we have to search for it
# this is where dictionaries come in

# dictionaries offer us key-value pairs
# main idea that we have a fast way to access data by a key
# we can acess, deleta or update data in any large dictionary in constant\
# Computer Science calls this O(1) time complexity
# so even in a huuuge dictionary, we can access data in the same time as a small one
# this is because dictionaries are implemented using hash tables

# latviski vārdnīca saturēs atslēgu-vērtību pārus

# other programming languages call dictionaries:
# hash maps, hash tables, associative arrays, maps

# main idea is to "instantly" access data by a key
# we can use any immutable data type as a key - typically strings or numbers
# but can also use tuples(we will talk about them today as well)

# some properties of dictionaries in Python:
# 1. dictionaries are mutable - we can change values in them
# 2. dictionaries are dynamic - we can add or remove items (key-value pairs)
# 3. dictionaries are unordered - the order of items is not guaranteed
# 3b. order actually is preserved in Python 3.7+
# 4. dictionaries are indexed by key - we can access items by key (not index)
# 5. dictionaries are iterable - we can loop through them
# 6. dictionaries can contain any data type as values - even other dictionaries
# 7. keys are unique - we cannot have duplicate keys in a dictionary
# 8. keys must be immutable - we cannot use lists or dictionaries as keys
# 9. values can be mutable - we can use lists or dictionaries as values
# 10. dictionaries can be nested - we can have dictionaries inside dictionaries
# 11. frequently dictionaries are used together with lists - 
# we can have lists of dictionaries or dictionaries of lists

# let's start by making an empty dictionary
# we can use curly braces or the dict() function
empty_dict = {} # most typical way of creating an empty dictionary
print(empty_dict)  # prints {}
also_empty_dict = dict() # dict function can be used to create also big dictionaries
print(also_empty_dict)  # prints {}
# how long are these dictionaries? - we can use the len() function to check the length of a dictionary
print(f"Empty dictionary length: {len(empty_dict)}")  # prints 0
print(f"Also Empty dictionary length: {len(also_empty_dict)}")  # prints 0

# let's create a dictionary with some data in them
# let's create a phone dictionary for Alice, Bob, Carol and David

phone_dict = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Carol": "555-8765",
    "David": "555-4321"
}

# let's print the dictionary
print(phone_dict)  # prints {'Alice': '555-1234', 'Bob': '555-5678', 'Carol': '555-8765', 'David': '555-4321'}
# let's print the length of the dictionary
print(f"Phone dictionary length: {len(phone_dict)}")  # prints 4

# let's get Alice's phone number
# we can access the value by using the key in square brackets
print("Alice's phone number", phone_dict["Alice"])  # prints 555-1234
# note this is a very quick way to access data in a dictionary no matter how big it is

# compare if we had data stored in phone_list with the same data
phone_list = [
    ["Alice", "555-1234"],
    ["Bob", "555-5678"],
    ["Carol", "555-8765"],
    ["David", "555-4321"]
]

# now to find "David" we would have to loop through the list and check each item
for item in phone_list:
    if item[0] == "David":
        print("David's phone number", item[1])  # prints 555-4321
        break  # we found David, so we can stop the loop
# this is a lot slower than accessing the dictionary directly

# okay so we know how to get data from a dictionary by key

# how about adding a new key say "Valdis" with a phone number "555-0000"
# we can do this by using the same syntax as getting data from a dictionary

phone_dict["Valdis"] = "555-0000"  # adds a new key-value pair to the dictionary
print(phone_dict)  # prints {'Alice': '555-1234', 'Bob': '555-5678', 'Carol': '555-8765', 'David': '555-4321', 'Valdis': '555-0000'}
# how many items are in the dictionary now?
print(f"Phone dictionary length: {len(phone_dict)}")  # prints 5

# mutating values in a dictionary
# let's add another number for Alice
phone_dict["Alice"] = "555-9999"  # updates the value for the key "Alice" by overwriting it
# there are ways to check if a key exists in a dictionary

# so how to check - so called existance check or membership test
# we can use the in keyword to check if a key exists in a dictionary
person = "Alice"
print(f"Is {person} in phone_dict? {person in phone_dict}")  # prints True

bad_person = "Voldemort"
print(f"Is {bad_person} in phone_dict? {bad_person in phone_dict}")  # prints False

# this leads to idea of how we could check if a key exists before reading data

# otherwise we get keyerror if we try to access a key that does not exist in the dictionary
try:
    print(phone_dict["Voldemort"])  # raises KeyError
except KeyError as e:
    print(f"KeyError: {e}")
# this is a common error when working with dictionaries 

# we could do the following
if "Voldemort" in phone_dict:
    print(phone_dict["Voldemort"])
else:
    print("Voldemort is not in the phone dictionary")

# for occassions when we are not sure if key exists in the dictionary
# we can use the get() method to access data in a dictionary
# get method returns None by default if key does not exist

print("Valdis's phone number", phone_dict.get("Valdis"))  # prints 555-0000
print("Voldemort's phone number", phone_dict.get("Voldemort"))  # prints None

# let's set default value for the get method - "not found"
print("Voldemort's phone number", phone_dict.get("Voldemort", "not found"))  # prints not found

# so again use get when we are not sure if key exists in the dictionary
# use [key] when we are sure key exists in the dictionary

# deleting items from a dictionary
# we use del dictionary[key] to delete an item from a dictionary
# let's delete Bob from the phone dictionary

del phone_dict["Bob"]  # deletes the key-value pair for Bob
print(phone_dict)  # prints {'Alice': '555-9999', 'Carol': '555-8765', 'David': '555-4321', 'Valdis': '555-0000'}

# however we can not delete non existing key from the dictionary
# this will raise a KeyError
try:
    del phone_dict["Bob"]  # raises KeyError
except KeyError as e:
    print(f"KeyError: {e}")

# this means we should check if key exists before deleting it
# or we can use pop method to delete an item from a dictionary
# pop method returns the value of the key that was deleted
if "Bob" in phone_dict:
    print(f"Deleting {phone_dict.pop('Bob')} from phone dictionary")  # prints Bob's phone number
    del phone_dict["Bob"]  # deletes the key-value pair for Bob
else:
    print("Bob is not in the phone dictionary")

# we can use variables for both or either key and value
key = "Eve"
value = "555-1111"
phone_dict[key] = value  # adds a new key-value pair to the dictionary
print(phone_dict)  # prints {'Alice': '555-9999', 'Carol': '555-8765', 'David': '555-4321', 'Valdis': '555-0000', 'Eve': '555-1111'}

# of course we can get value by key
print(f"{key}'s phone number", phone_dict[key])  # prints Eve's phone number

# so how about looping through our phone numbers

# we have a couple of ways
# we can loop through:
# 1. keys - this is default behaviour of the dictionary - same as keys() method
# 2. values - we can use values() method to get all values in the dictionary
# 3. items - we can use items() method to get all key-value pairs in the dictionary

# so syntax for looping through keys is simply
# for key in dictionary:
for key in phone_dict: # key is just a name for variable, could be any valid name such k for example
    print(key, "--->", phone_dict[key])  # prints all keys AND values in the dictionary
    # note that we did not have to use get() method or check if key exists in the dictionary
    # this is because we are looping through the dictionary and Python knows that key exists

# less common is just go through values only
for value in phone_dict.values():
    print(value)  # prints all values in the dictionary
    # this is less used because we generally want the key-value pairs
    # but we can use this if we only care about the values

# this means I can get a list of values and also keys if I want

key_list = list(phone_dict.keys())  # gets a list of keys in the dictionary
print(key_list)  # prints ['Alice', 'Carol', 'David', 'Valdis', 'Eve']
value_list = list(phone_dict.values())  # gets a list of values in the dictionary
print(value_list)  # prints ['555-9999', '555-8765', '555-4321', '555-0000', '555-1111']
# these lists are not related to the original dictionary anymore
# so we can modify them without affecting the original dictionary

# very common when iterating is to want both key and value at the same time
# this is where items() method comes in handy
# it returns a list of tuples with key-value pairs
# typical syntax is:
# for key, value in dictionary.items():

for key, value in phone_dict.items():  # key and value are just names for the variables
    print(key, "--->", value)  # prints all keys AND values in the dictionary

# same result would be if we used the following syntax
# i could have named the key person and value phone_number for example
for person, phone_number in phone_dict.items():  # key and value are just names for the variables
    print(person, "--->", phone_number)  # prints all keys AND values in the dictionary