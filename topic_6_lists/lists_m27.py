# We already know our basic primitive data types:
# int, float, str, bool
# We also know that we can create variables of these types:

# there are other more complex data types that are built from these primitive data types

# why would we want to do that?
# let's say we want to store a shopping list
# we could create a variable for each item in the list
item_1 = "milk"
item_2 = "eggs"
item_3 = "bread"
item_4 = "butter"
item_5 = "cheese"

# we are talking about the same type of data here
# what do we do when we need 100 or 1000 items or millions of items?
# we could create a variable for each item in the list but that would be rather silly

# instead Python offers as a solution a data type called a list
# a list is a collection of items - in other languages it is called an array
# a list can contain any number of items and each item can be of any type
# best use of a list is to store items of a similar type such as str or int
# but we can also mix types in a list if needed


shopping_list = ["milk 🥛", "eggs 🥚", "bread 🍞"]
# this is a list of strings 
print(shopping_list)
print(type(shopping_list))

# so what can we do with a list?

# 1. we can create a list - like we just did
# 2. we can access items in a list - by index
# 3. we can check if an item is in a list - using the in operator
# 4. we can modify contents of some item in a list - mutable by index
# 5. we can add items to a list - using append() method
# 6. we can remove items from a list - using remove() method
# 7. we can sort a list - using sort() method
# 8. we can reverse a list - using reverse() method 
# 9. we can join two lists - using + operator
# 10. we can repeat a list - using * operator
# 11. we can slice a list - using [start:end] syntax
# 12. we can iterate over a list - using for loop
# 13. we can find the length of a list - using len() function
# 14. we can find the index of an item in a list - using index() method
# 15. we can nest lists - using list inside a list
# 16. advanced - list comprehension - creating a list from another list using a single line of code

empty_list = [] # empty list we use square brackets to create a list
print(empty_list)
# we can add items to any list later

# let's look at our shopping list by index - 0 based index
print(shopping_list[0]) # first item in the list - index starts from 0
print(shopping_list[1]) # second item in the list
print(shopping_list[2]) # third item in the list

# how many items do I have in my shopping list?
print(f"I have {len(shopping_list)} items in my shopping list")

# again we have negative indexing if we want to use from end of the list
print(f"Last item to buy is {shopping_list[-1]}")

# let's check whether we have bread
print("Do we have bread?", "bread 🍞" in shopping_list)
# the match has to be exactly the same - including the emoji
# if you need not exact match then we will need to loop about that later

# how about beer?
print("Do we have beer?", "beer 🍺" in shopping_list)

# let's use some numbers to demonstrate slicing
numbers = list(range(0, 120, 10)) # create a list of numbers from 0 to 110 with step of 10
# note we use list to convert range to a list
# range is iterable /loopable thus we can create a list from it
print(numbers) # print the list of numbers

first_3 = numbers[:3] # first 3 items in the list - 0 is default start index
# this is the same as numbers[0:3]
print(first_3) # print the first 3 items in the list
last_3 = numbers[-3:] # last 3 items in the list - 
# no end index means to the end of the list
print(last_3) # print the last 3 items in the list

# we can also reverse the list using slicing
reversed_numbers = numbers[::-1] # start at the end and go to the beginning
print(reversed_numbers) # print the reversed list

# let's change some item in our shopping list using index
# first let's print the list
print(shopping_list) # print the shopping list
# let's change milk to kefir
shopping_list[0] = "kefir 🥛" # change the first item in the list
print(shopping_list) # print the shopping list again

# we only have 3 items in our shopping
# what happens if we try index 3 for example which symbolizes 4th item?
try:
    print(shopping_list[3]) # this will raise an error
except IndexError as e:
    print("Error:", e)

# if I do not want to use try I could just check len(my_list) first

# how could I add items to my shopping list
# one way is to use + operator to join two lists
# let's say I want to add some more items to my shopping list
more_items = ["beer 🍺", "wine 🍷", "whiskey 🥃"]
new_shopping_list = shopping_list + more_items # join two lists
print(new_shopping_list) # print the new shopping list
# above is so called OUT OF PLACE modification of the list
# OUT OF PLACE means we create a new list and assign it to a new variable

# let's create a list of Latvian beers
latvian_beers = ["Aldaris", "Cēsu", "Lāčplēsis", "Valmiermuiža"]
print(latvian_beers) # print the list of Latvian beers

# let's add 'Labietis'
latvian_beers.append("Labietis") # add item to the end of the list
print(latvian_beers) # print the list of Latvian beers again
# note I did not use = operator here
# i simply used append() method to add item to the list
# this is is called IN-PLACE modification of the list
# how many beers do I have now?
print(f"I have {len(latvian_beers)} beers in my list")

# what happens if we try to append three beers at once
latvian_beers.append(["Bauskas", "Tērvetes", "Brālis"])
# results might not be quite what you want
print(latvian_beers) # print the list of Latvian beers again
# turns out I've appended a list to the list
# I've created a nested list
# probably you do not want it here
# now if i wanted to get last item from last item in the list
print(latvian_beers[-1][-1]) # this will print 'Brālis'

# let's remove our last item from the list
# but I also want to save it

# to do so we use pop() method
# pop() method removes the last item from the list and returns it
# returns means we can save it to a variable if we want to
last_3 = latvian_beers.pop() # remove last item from the list and save it to a variable
print(last_3) # print the last item we just removed from the list
# print the list of Latvian beers again
print(latvian_beers) # print the list of Latvian beers again

# if I want to flatly add another list to existing list I use extend() method
# let's say I want to add some more beers to my list
# so lets add those last 3 beers to my list
latvian_beers.extend(last_3) # add last 3 beers to the list
print(latvian_beers) # print the list of Latvian beers again

# now let's remove the first item from the list using pop()
# pop() method removes the last item from the list by default
#  but we can also specify the index of the item we want to remove

# let's remove the first item from the list
first_item = latvian_beers.pop(0) # remove first item from the list and save it to a variable
print(first_item) # print the first item we just removed from the list
# print the list of Latvian beers again
print(latvian_beers) # print the list of Latvian beers again

# i could also use remove
# remove() method removes the first item from the list that matches the value we provide
# let's remove 'Cēsu' from the list
latvian_beers.remove("Cēsu") # remove 'Cēsu' from the list
print(latvian_beers) # print the list of Latvian beers again 

# let's add Brengulis but let's add it somewhere in middle say index 2 - 3rd item
# we can use insert() method to add item to the list at specified index
# insert() method takes two arguments - index and value
# let's add 'Brengulis' to the list at index 2
latvian_beers.insert(2, "Brengulis") # add 'Brengulis' to the list at index 2
print(latvian_beers) # print the list of Latvian beers again

# I should add that inserting items in beginning or middle of the list is not very efficient for LARGE list

brengulis_index = latvian_beers.index("Brengulis") # find index of 'Brengulis' in the list
print(brengulis_index) # print the index of 'Brengulis' in the list

# let's add another Brengulis to the end of the list
latvian_beers.append("Brengulis") # add 'Brengulis' to the end of the list
latvian_beers.append("Brengulis") # add 'Brengulis' to the end of the list
# of course I could have used extend() method to add a list of items to the list

print(latvian_beers) # print the list of Latvian beers again

# we can count how many Brengulis we have in the list using count() method
print(f"I have {latvian_beers.count('Brengulis')} Brengulis in my list") # print the number of 'Brengulis' in the list
# so let me show you a little recipe on how to keep only required number of items

how_many_to_keep = 1 # how many Brengulis do I want to keep in the list
# if I wanted none I would enter 0 above
# let's say I want to keep only 1 Brengulis in the list
while latvian_beers.count("Brengulis") > how_many_to_keep:
    latvian_beers.remove("Brengulis") # remove 'Brengulis' from the list
print(latvian_beers) # print the list of Latvian beers again
# again not super effective on huge lists

# now let's talk about loops and iteration
# we use for loop to go through list items one by one
for beer in latvian_beers:
    print(beer, end="-🍺-") # print each beer in the list and use custom end symbol
print()


# it is very common to want to filter or do some sort of work on list items
# so one workflow is to start with empty list for storing results
# and then append items to it one by one based on some condition
# for now we use standard loop

# now let's get beers that only start with letter B
b_beers = [] # create empty list for storing results
for beer in latvian_beers: # loop through each beer in the list
    if beer.startswith("B"): # check if beer starts with letter B - use whatever condition you want
        b_beers.append(beer) # add beer to the results list

print(b_beers) # print the list of beers that start with letter B
# simple filtering of the list
# there is another syntax called list comprehension about that later

# how about getting index of whichever element when looping
# we have two approaches
# one Non Pythonic way is to use range() and len() to get index of each item in the list
for i in range(len(latvian_beers)):
    print(f"Beer {i} is {latvian_beers[i]}") # print index and beer name
# this is not very Pythonic way of doing things

# more Pythonic is to use enumerate() function
# enumerate() function adds a counter to the iterable and returns it in the form of enumerate object

for i, beer in enumerate(latvian_beers):
    print(f"Beer {i} is {beer}") # print index and beer name
# this is more Pythonic way of doing things

# turns out we do not need index that often

# remember we could do the same with strings
for i, c in enumerate("Valdis"):
    print(f"Character {i} is {c}") # print index and character

# now let's discuss alias and copy of lists
# for primitive data types like int, float, str, bool we know that assignment operator = creates a copy of the value
# but with lists it is different

beer_list_alias = latvian_beers # this creates an alias to the same list
# under neath beer_list_alias and latvian_beers are pointing to the same list in memory
# if you do need a copy we use a copy method
beer_list_copy = latvian_beers.copy() # this creates a copy of the list
# let's print all 3 for now
print("Beer list alias and copy")
print(latvian_beers) # print the original list
print(beer_list_alias) # print the alias of the list
print(beer_list_copy) # print the copy of the list

# we can compare contents using == operator
print("Does alias have same contents as original?")
print(latvian_beers == beer_list_alias) # True - same contents, of course
print("Does copy have same contents as original?")
print(latvian_beers == beer_list_copy) # True - same contents, of course
# is alias same item in memory 
print("Is alias same item in memory as original?")
print(latvian_beers is beer_list_alias) # True - same item in memory
print("Is copy same item in memory as original?")
print(latvian_beers is beer_list_copy) # False - different item in memory

# let's sort our latvian_beers list
# first let me show you how to create a new list using sorted()
sorted_list = sorted(latvian_beers) # this creates a new sorted list
print("Sorted list of beers")
print(sorted_list) # print the sorted list of beers
# original list is unchanged
print("Original list of beers")
print(latvian_beers) # print the original list of beers
# also alias and the copy is not changed
print("Alias list of beers")
print(beer_list_alias) # print the alias list of beers
print("Copy list of beers")
print(beer_list_copy) # print the copy list of beers

# now I will use sort method - this is IN PLACE it modifies the original!
# so be careful with that
latvian_beers.sort() # this sorts the original list in place
print("Sorted list of beers")
print(latvian_beers) # print the sorted list of beers
# alias is ALSO affected! it is the same list!
print("Alias list of beers")
print(beer_list_alias) # print the alias list of beers
# copy is not affected
print("Copy list of beers")
print(beer_list_copy) # print the copy list of beers

# we also have clear IN PLACE
# it will clear ALL elements from the list
# so be careful with that
latvian_beers.clear() # this clears the original list in place
print("Cleared list of beers")
print(latvian_beers) # print the cleared list of beers
# alias is also cleared
print("Alias list of beers")
print(beer_list_alias) # print the alias list of beers
# copy is not affected
print("Copy list of beers")
print(beer_list_copy) # print the copy list of beers

# now remember I talked how nice it is to have same data type
# for all numeric lists then we get access to some nice functions
# sum, min, max (others are available in math module)

# let's print our numbers list again
print(numbers) # print the list of numbers
# let's sum all numbers in the list
print("Sum of numbers:", sum(numbers)) # print the sum of numbers in the list
# i could have done tis with loop of course
total = 0 # create a variable for total
for number in numbers: # loop through each number in the list
    total += number # add number to total
print("Sum of numbers:", total) # print the sum of numbers in the list

numbers.append(-50) # add a negative number to the list

# and then we have min and max as well for numeric lists
print("Min number:", min(numbers)) # print the min number in the list
print("Max number:", max(numbers)) # print the max number in the list


# if I did not have this type of function what could I do?
my_min = numbers[0] # create a variable for min number
for number in numbers[1:]: # loop through each number in the list starting from second
    if number < my_min: # check if number is less than min number
        my_min = number # set min number to current number
print("Min number:", my_min) # print the min number in the list
