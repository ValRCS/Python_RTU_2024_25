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


shopping_list = ["milk", "eggs", "bread", "butter", "cheese"]
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