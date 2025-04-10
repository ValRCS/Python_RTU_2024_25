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