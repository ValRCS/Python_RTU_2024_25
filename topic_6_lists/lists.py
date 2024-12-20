# so far we know primitive data types
# such as int, float, str, bool
# what happens if we have many similar data types?
# if we do not know any better we could try this...
a1 = 1
a2 = 2
a3 = 3
a4 = 5
a5 = 8
a6 = 13
# this is of course Fibonacci sequence
# what if we have 100, or 1000 numbers?

# instead Python offers us a list data type - this is similar to arrays in other languages
# not to be confused with linked list - that is a different data structure

# Python saraksti ir saraksts ar elementiem, kas ir sakartoti un numurēti, sākot ar 0

# main idea behind lists is that we can store multiple values in a single variable
# what can we do with lists?
# 1. create a list
# 2. access elements of a list
# 3. change elements of a list - mutable
# 4. add elements to a list - dynamic size / resizable
# 5. remove elements from a list - dynamic size / resizable
# 6. iterate through a list
# 7. sort a list
# 8. search for elements in a list
# 9. some other operations

# we will see that some things are quite similar to string operations

# first let's create a list - for now empty
# we can create a list by using square brackets []
my_list = [] # so this is an empty list
print(my_list) # []

# how many elements are in the list?
print(f"Number of elements in the list: {len(my_list)}") # 0 # remember len also worked on strings

# let's make a shopping list
shopping_list = ["milk", "bread", "eggs", "butter"]
print(shopping_list) # ['milk', 'bread', 'eggs', 'butter']
# lists do not mandate same data type - unlike many other languages
# we could mix and match different data types
mixed_list = [1, "two", 3.0, True]
print(mixed_list) # [1, 'two', 3.0, True] 
# in general we try to avoid mixing types if possible

# how big is our shopping list?
print(f"Number of elements in the shopping list: {len(shopping_list)}") # 4

# so syntax to create a list is as follows:
# list_name = [element1, element2, element3, ..., elementN]
# elements could be literals or could be other variables
food = "apple"
drink = "kefir"
# so shopping list with variables and literals
shopping_list = [food, "bread", drink, "butter"] # I overwrite my old list
print(shopping_list) # ['apple', 'bread', 'kefir', 'butter']
print(f"Number of elements in the shopping list: {len(shopping_list)}") # 4

# let's access some elements of the list
# we use the SAME syntax as with strings - 0 based index
# so first item is at index 0
print(f"First item in the shopping list: {shopping_list[0]}") # apple
# how about last - two ways of doing it
print("Last item", shopping_list[3], shopping_list[-1]) # butter butter
# of course I can save this last item in a variable
last_item = shopping_list[-1]
print("Last item", last_item) # butter

# so just like strings we can use slicing same way
# so first two items
print("First two items", shopping_list[:2]) # ['apple', 'bread']
# last three
print("Last three items", shopping_list[-3:]) # ['bread', 'kefir', 'butter']

# let's get a list of numbers from 0 to 90 with step 10
numbers = list(range(0, 100, 10)) # so range gives you half ready list - you need to convert it to list
# range is not always needed to convert to list - we can use range to loop without converting
print(numbers) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# so let's get middle two elements
middle_two = numbers[4:6] # so 40 and 50
print(middle_two) # [40, 50]
# note middle_two is a list with two elements , slices return lists from lists
# every 2nd element
print("Every 2nd element", numbers[::2]) # [0, 20, 40, 60, 80]
# every 3rd element starting from 10 - so 10, 40, 70
print("Every 3rd element", numbers[1::3]) # [10, 40, 70]

reversed_numbers = numbers[::-1] # so this is a common way to reverse a list
print(reversed_numbers) # [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# okay some more examples
# let's get 2nd, 3rd and 4th element
# this means we start at index 1 and end at index 4 - 
# index 4 is not included because that would be the 5th element
print("2nd, 3rd and 4th element", numbers[1:4]) # [10, 20, 30]
# now last 5 elements - let's use negative indexing
# so we start at index -5 and go to the end as default
print("Last 5 elements", numbers[-5:]) # [50, 60, 70, 80, 90]
# again first 3 would be 0, 10, 20 - so we start at 0 and go to index 3
# we do not need to specify the start index if we start at 0
print("First 3 elements", numbers[:3]) # [0, 10, 20]

# note slicing creates a new list - it does not modify the original list

# now let's change some element in the list
# print my shopping list
print(shopping_list) # ['apple', 'bread', 'kefir', 'butter']
# let's change bread to cheese
shopping_list[1] = "cheese" # so I change 2nd element with index 1 to cheese
# this is not possible with strings - strings are immutable
print(shopping_list) # ['apple', 'cheese', 'kefir', 'butter']
# let's change last element to olive oil
# we could use 3 or -1
shopping_list[-1] = "olive oil"
print(shopping_list) # ['apple', 'cheese', 'kefir', 'olive oil']

# so we can mutate lists - change elements

# we can also add elements to the list - dynamic size

# let's add some items to the shopping list
# we can use append method - this adds element to the end of the list
# let's add tomatoes
shopping_list.append("tomatoes") # note we are not saving the result - append MODIFIES the list itself
# in Computer Science this is called IN PLACE operation - we modify the original object - nothing new is created
print(shopping_list) # ['apple', 'cheese', 'kefir', 'olive oil', 'tomatoes']
# what happens if we try to append two things with append
# let's add ravioli and bread sticks
shopping_list.append(["ravioli", "bread sticks"]) 
# we might not get what we wanted
print(shopping_list) # ['apple', 'cheese', 'kefir', 'olive oil', 'tomatoes', ['ravioli', 'bread sticks']]
# we've created a nested list a list inside a list
# most likely we do not want it here

# instead we can use extend method to add multiple elements as separate elements
# first let's pop the last element out of the list
last_element = shopping_list.pop() # so pop removes the last element and returns it
# again pop modifies the list in place
print(last_element) # ['ravioli', 'bread sticks']
print(shopping_list) # ['apple', 'cheese', 'kefir', 'olive oil', 'tomatoes']

# so now we can use extend
shopping_list.extend(["ravioli", "bread sticks", "wine"]) # so we add 3 elements in a flat way
# again this modifies the list in place
print(shopping_list) # ['apple', 'cheese', 'kefir', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']


# let's find out index of kefir
# we can use index method
index_kefir = shopping_list.index("kefir") # this raises an error if element is not found
print("kefir is at index", index_kefir) # 2
# there is no find method - index is the method to use for lists
shopping_list.remove("kefir") # so we remove kefir from the list, raises an error if element is not found
print(shopping_list) # ['apple', 'cheese', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']
# let's check if kefir is in the list
# we can use in operator
if "kefir" in shopping_list:
    print("kefir is in the list")
else:
    print("kefir is not in the list")

#let's add one more apple to the list but let's insert it at index where kefir was
shopping_list.insert(index_kefir, "apple") # so we insert apple at index 2
# rest of values will be shifted to the right
print(shopping_list) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']
# this insert can be inefficient - if you need to insert at the beginning or end of very large list
# append is more efficient and faster

# let's count how many apples we have in the list
print("There are", shopping_list.count("apple"), "apples in the list") # 2

# now let's talk copy and alias
# if we use assignment operator = we create an alias, a shortcut to the same list but not new list!
shopping_list_alias = shopping_list # we have two names for the same list
# if we change one list the other will change as well
# now let's create a real copy
shopping_list_copy = shopping_list.copy() # so we create a new list with the same elements
# let'' print all 3
print(shopping_list) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']
print(shopping_list_alias) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']
print(shopping_list_copy) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']

print("Will sort original list")
# let's sort the original list - lexigraphical order
shopping_list.sort() # so we sort the list in place, we modify the original list

# let's print all 3
print("shopping_list", shopping_list) # ['apple', 'apple', 'bread sticks', 'cheese', 'olive oil', 'ravioli', 'tomatoes', 'wine']
print("shopping_list_alias", shopping_list_alias) # ['apple', 'apple', 'bread sticks', 'cheese', 'olive oil', 'ravioli', 'tomatoes', 'wine']
print("shopping_list_copy", shopping_list_copy) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']

# let's clear alias - careful with clear! it modifies the original list
shopping_list_alias.clear() # so we clear the list - we modify the original list as well...
print("shopping_list", shopping_list) # []
print("shopping_list_alias", shopping_list_alias) # []
print("shopping_list_copy", shopping_list_copy) # ['apple', 'cheese', 'apple', 'olive oil', 'tomatoes', 'ravioli', 'bread sticks', 'wine']

print("I am hungry, let's go to the store")
# let'' iterate over a list
for item in shopping_list_copy: # item could be element, it, i, x, t, any variable name
    print("I need to buy", item)