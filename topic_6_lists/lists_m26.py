# So we know our basic primitive data types
# we have int, float, str, bool
# but we also have a more complex data type called a list

# why should we need a list?
# let's see we want to store some numbers
a1 = 1
a2 = 2
a3 = 3
a4 = 5
a5 = 8
a6 = 13
# what do I do if I need to store 100 ? or 1 million numbers?

# to solve this Python  offers a list data type
# a list is a collection of items, a sequence of items
# a list can contain any data type, including other lists
# best use of lists is to store a collection of items of the same type


# what can we do with lists?
# 1. create a list
# 2. access items in a list - index based access
# 2a. - check for existence of an item in a list - membership operator
# 3. modify items in a list - mutable
# 4. add items to a list - dynamic size / resizable
# 5. remove items from a list - dynamic size / resizable
# 6. sort a list
# 7. reverse a list
# 8. iterate over a list - loop through a list
# 9. list comprehension - create a list from another list
# 10. other list methods - built in functions to work with lists
# 11. nested lists - list of lists
# 12. list slicing - get a sublist from a list


# let's create an empty list
my_list = [] # empty list
print(my_list) # prints []
print(type(my_list)) # prints <class 'list'>

# let's start by finding a number of elements in our list
print(f"Length of my_list: {len(my_list)}") # prints 0

# let's create a shopping list with some items in it
shopping_list = ["milk", "eggs", "bread", "butter"]
print(shopping_list) # prints ['milk', 'eggs', 'bread', 'butter']

# i could have made mixed list
mixed_list = ["milk", 2, 3.14, True, None, [1, 2, 3]]
print(mixed_list) # prints ['milk', 2, 3.14, True, None, [1, 2, 3]]
print(type(mixed_list)) # prints <class 'list'>
# in general try to avoid mixed lists if you can

# again how big is our shopping list?
print(f"Length of shopping_list: {len(shopping_list)}") # prints 4

# we can use variables when creating a list
food = "chocolate"
drink = "coffee"
snack = "chips"
# let's recreated our shopping list
shopping_list = [food, drink, "bread", snack] # so I have recreated my shopping list using some variables
print(shopping_list) # prints ['chocolate', 'coffee', 'bread', 'chips']

# membership check in a list
print("Do we need to buy milk?", "milk" in shopping_list) # prints False
print("Do we need to buy bread?", "bread" in shopping_list) # prints True

# note membership operator is case sensitive and it is exact match only
# later we can talk how do do partial matches

# Access
# indexing - we can access items in a list using index
# indexing starts from 0  just like strings

print(f"First item to buy is: {shopping_list[0]}") # prints chocolate
# how about last item?
# we could use positive index - 3
print(f"Last item to buy is: {shopping_list[3]}") # prints chips
# but what if we don't know the size of the list? we could use then negative index
# -1
print(f"Last item to buy is: {shopping_list[-1]}") # prints chips

# Slicing lists - works very similar to strings

# let's create a list of numbers from 0 to 90 by step 10
numbers = list(range(0, 100, 10)) # so list will create a list from any iterable object
# in this case we are using range object as an iterable
print(numbers) # prints [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# now let's get first 3 numbers
# we will store the result in a variable called first_3 - this is a copy of the first 3 numbers
first_3 = numbers[:3] # so we are slicing the list from 0 to 3 (not including 3)
print(first_3) # prints [0, 10, 20]
last_3 = numbers[-3:] # so we are slicing the list from -3 to end of the list
print(last_3) # prints [70, 80, 90]

# how about every 2nd number from the list?
# we can use step in slicing
# so we can use [start:end:step] syntax

every_2nd = numbers[::2] # so we are slicing the list from 0 to end of the list with step 2
print(every_2nd) # prints [0, 20, 40, 60, 80]

reversed_list = numbers[::-1] # so we are slicing the list from end to start with step -1
print(reversed_list) # prints [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# again slicing does not modify the original list!

# modifying item in a list
# unlike strings we can modify content of a list
print(shopping_list) # prints ['chocolate', 'coffee', 'bread', 'chips']
# let's change some items in our shopping list
shopping_list[0] = "juice" # so we are changing first item in the list
print(shopping_list) # prints ['juice', 'coffee', 'bread', 'chips']

# how about changing chips to something healthier?
shopping_list[-1] = "fruit" # so we are changing last item in the list
print(shopping_list) # prints ['juice', 'coffee', 'bread', 'fruit']

# so what happens if we try to acces non existing item in the list?
# let's try to access item at index 4
try:
    print(shopping_list[4]) # this will raise an error
except IndexError as e:
    print(f"Error: {e}")

# similary the empty list we can not access anything
print(my_list, len(my_list)) # prints [] 0
try:
    print(my_list[0]) # this will raise an error since we have no 1st element
except IndexError as e:
    print(f"Error: {e}")

# so simple looping over a list
# we can use for loop to iterate over a list
for n in numbers: # so we are iterating over the list
    print(n, end=" ") # prints 0 10 20 30 40 50 60 70 80 90
print() # prints new line

# if I wanted only values between 30 and 50 printed then I could use if inside for loop
for n in numbers:
    if n >= 30 and n <= 50:
        print(n, end=" ")
        # so here we could do whatever we need to do when we have specific numbers
print() # prints new line

# note about list from string
name = "Valdis"
name_list = list(name) # so we are creating a list from string
print(name_list) # prints ['V', 'a', 'l', 'd', 'i', 's']

# back to shopping list
# how do we add new items without replacing existing items?
# also we want to use existing list and not create a new one
# we can use append method to add new items to the list

# let's append something healthy again
shopping_list.append("walnuts") # so we are adding new item to the end of the list
print(shopping_list) # prints ['juice', 'coffee', 'bread', 'fruit', 'walnuts']
# Note the syntax we used shopping_list.append("walnuts") - we are calling append method on the shopping_list object
# this is so called IN-PLACE operation - we are modifying the existing object and not creating a new one
# print new size
print(f"Length of shopping_list: {len(shopping_list)}") # prints 5

# there is an alternative way where we would recreate the  list using + operator
shopping_list = shopping_list + ["soda"] # so we are creating a new list by adding new item to the existing list
print(shopping_list) # prints ['juice', 'coffee', 'bread', 'fruit', 'walnuts', 'soda']
# this is less efficient than using append method since we are creating a new list and copying all items to the new list
# so we are creating a new list and not modifying the existing one

# so unless I need a new list, append would be preferable

# ok let's create a list of Latvian beers
beer_list = ["Aldaris", "Cēsu", "Lāčplēsis", "Valmiermuiža", "Tērvetes"]
print(beer_list) # prints ['Aldaris', 'Cēsu', 'Lāčplēsis', 'Valmiermuiža', 'Tērvetes']
# let's add Labietis to the list
beer_list.append("Labietis") # so we are adding new item to the end of the list
print(beer_list) # prints ['Aldaris', 'Cēsu', 'Lāčplēsis', 'Valmiermuiža', 'Tērvetes', 'Labietis']

# so now what happens if I add two beers at once with append?
# let's try to append two beers at once
beer_list.append(["Bauskas", "Brālis"]) # so we are adding new item to the end of the list
print(beer_list) # prints ['Aldaris', 'Cēsu', 'Lāčplēsis', 'Valmiermuiža', 'Tērvetes', 'Labietis', ['Bauskas', 'Brālis']
# so we added a list inside a list - nested, that might not be what we want here

# let's fix this with a new method called pop
# pop method removes the last item from the list and returns it - again IN-PLACE operation modifying the existing list
mini_list = beer_list.pop() # so we are removing the last item from the list and storing it in a variable
print(mini_list) # prints ['Bauskas', 'Brālis']
# print beer list again
print(beer_list) # prints ['Aldaris', 'Cēsu', 'Lāčplēsis', 'Valmiermuiža', 'Tērvetes', 'Labietis']

# so let's use extend method to add two beers at once
# extend method adds items from another list to the end of the list
# so we can use it to add multiple items at once
beer_list.extend(mini_list) # so we are adding items from mini_list to the end of the beer_list
print(beer_list) # prints ['Aldaris', 'Cēsu', 'Lāčplēsis', 'Valmiermuiža', 'Tērvetes', 'Labietis', 'Bauskas', 'Brālis']

# so again difference between append and extend is that append adds a single item to the end of the list and extend adds multiple items from another list to the end of the list
# so we can use append to add a single item and extend to add multiple items at once