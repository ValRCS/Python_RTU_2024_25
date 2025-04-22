# Let's talk about sets (kopa - Latvian)
# set is a collection of unique elements - unordered!
# note similarities with dictionaries - keys have to be unique as well

# Some set properties:
# - unordered collection of unique elements
# - mutable (can be changed) - add or remove elements
# - no duplicates allowed
# - no indexing or slicing (like lists)
# - can be used for membership testing (in operator) - QUICKER than lists
# - can be used for set operations (union, intersection, difference, etc.)

# - oficial set tutorial: https://docs.python.org/3/tutorial/datastructures.html#sets
# - set operations: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

# we can create a set from say strings, lists, tuples, dictionaries, etc.
# but we can also create an empty set using set() function

# let's start with a set from a string
char_set = set("hello pausaule")
print(char_set)  # {' ', 'a', 'e', 'h', 'l', 'o', 'p', 's', 'u'} in RANDOM order

# how long is the set?
print(f"Length of the set: {len(char_set)}")  # 9 - no duplicates

# one use is to check for existence of an element in the set
print(f"Is 'h' in the set? {'h' in char_set}")  # True
print(f"Is 'x' in the set? {'x' in char_set}")  # False

# these membership tests are much faster than in lists or tuples
# in Computer Science, we call this O(1) - constant time complexity
# (in lists and tuples, it is O(n) - linear time complexity)

# so if you have data with frequent membership tests, use sets instead of lists or tuples
# but remember that sets are unordered, so you cannot access elements by index

# how about set of uniques from a list?
foods = ["apple", "banana", "orange", "apple", "banana", "kiwi"]
print(foods)  # ['apple', 'banana', 'orange', 'apple', 'banana', 'kiwi']
unique_foods_set = set(foods)
print(unique_foods_set)  # {'banana', 'kiwi', 'orange', 'apple'} # again in RANDOM order
print(f"Length of the set: {len(unique_foods_set)}")  # 4 - no duplicates

# note how sets also use {} brackets, but they are not the same as dictionaries
# dictionary syntax is {key: value, key: value, ...}
# sets are just {value, value, ...} - no key-value pairs

# so now that we have unique foods, let's go back to a list
# it is as easy as using the list() function
unique_foods_list = list(unique_foods_set)
print(unique_foods_list)  # ['banana', 'kiwi', 'orange', 'apple'] - again in RANDOM order

# let's add some foods to my unique foods set
unique_foods_set.add("mango")
unique_foods_set.add("kiwi")  # kiwi is already in the set, so it won't be added again
print(unique_foods_set)  # {'banana', 'kiwi', 'orange', 'apple', 'mango'}

# let's remove some foods from my unique foods set
unique_foods_set.remove("banana")  # remove banana from the set
print(unique_foods_set)  # {'kiwi', 'orange', 'apple', 'mango'}

# so since remove raises Key Error we have two approaches:

unique_foods_set.discard("banana")  # discard does not raise Key Error if element is not found
print(unique_foods_set)  # {'kiwi', 'orange', 'apple', 'mango'}

# 2nd approach would be to use try/except block
try:
    unique_foods_set.remove("banana")
except KeyError as e:
    print(f"KeyError: {e} - element not found in the set") 

# so it is typical to create unique lists from sets and vice versa

# now let's talk about set operations

# let's create some numbers first
numbers_0_9 = set(range(10))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numbers_0_9)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# how about 3 to 7
num_3_7 = {3,4,5,6,7,3,3,3,3,6} # note thisi syntax is also valid
print(num_3_7)  # {3, 4, 5, 6, 7} - no duplicates

# let's compare {} with set ()
num_5_9 = set([5,6,7,9,6,8,8,9]) # we pass a list to set() function
print(num_5_9)  # {5, 6, 7, 8, 9} - no duplicates

# let's see if one set is subset of another
print(f"Is {num_3_7} subset of {numbers_0_9}? {num_3_7.issubset(numbers_0_9)}")  # True
print(f"Is {numbers_0_9} subset of {num_3_7}? {numbers_0_9.issubset(num_3_7)}")  # False

# Python offers us syntax sugar for this operation
print(f"Is {num_3_7} <= {numbers_0_9}? {num_3_7 <= numbers_0_9}")  # True
print(f"Is {numbers_0_9} <= {num_3_7}? {numbers_0_9 <= num_3_7}")  # False

# we also have strict subset operation
print(f"Is {num_3_7} < {numbers_0_9}? {num_3_7 < numbers_0_9}")  # True 
print(f"Is {numbers_0_9} < {num_3_7}? {numbers_0_9 < num_3_7}")  # False
# how about set being a strict subset of itself?
print(f"Is {num_3_7} < {num_3_7}? {num_3_7 < num_3_7}")  # False - it is not a strict subset of itself
print(f"Is {num_3_7} <= {num_3_7}? {num_3_7 <= num_3_7}")  # True - it is a subset of itself
# strict subset means that the set is not equal to the other set
# so if we have two sets, we can check if they are equal or not
print(f"Is {num_3_7} == {numbers_0_9}? {num_3_7 == numbers_0_9}")  # False

# note we could also go the other way superset
# so we can check if one set is superset of another
print(f"Is {numbers_0_9} superset of {num_3_7}? {numbers_0_9.issuperset(num_3_7)}")  # True
print(f"Is {num_3_7} superset of {numbers_0_9}? {num_3_7.issuperset(numbers_0_9)}")  # False
print(f"Is {numbers_0_9} >= {num_3_7}? {numbers_0_9 >= num_3_7}")  # True
print(f"Is {num_3_7} >= {numbers_0_9}? {num_3_7 >= numbers_0_9}")  # False
print(f"Is {num_3_7} >= {num_3_7}? {num_3_7 >= num_3_7}")  # True - it is a superset of itself
print(f"Is {num_3_7} > {num_3_7}? {num_3_7 > num_3_7}")  # False - it is not a strict superset of itself

# so let's get to main operations 
# union, intersection, difference, symmetric difference

#  union - combine two sets into one set with all unique elements contained from both sets

num_3_9 = num_3_7.union(num_5_9)  # {3, 4, 5, 6, 7, 8, 9}
print(f"Union of {num_3_7} and {num_5_9} is {num_3_9}")  # {3, 4, 5, 6, 7, 8, 9}
# we also have a syntax sugar for this operation - the | operator
print(f"Union of {num_3_7} and {num_5_9} is {num_3_7 | num_5_9}")  # {3, 4, 5, 6, 7, 8, 9}

# then we also have intersection - common elements between two sets
# Latviski intersection - šķēlums
num_5_7 = num_3_7.intersection(num_5_9)  # {5, 6, 7}
print(f"Intersection of {num_3_7} and {num_5_9} is {num_5_7}")  # {5, 6, 7}
# we also have a syntax sugar for this operation - the & operator
# note similarities with && in other languages - And operator
print(f"Intersection of {num_3_7} and {num_5_9} is {num_3_7 & num_5_9}")  # {5, 6, 7}

# we also have difference - elements in one set that are not in the other set
# Latviski difference - atšķirība
num_3_4 = num_3_7.difference(num_5_9)  # {3, 4}
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_4}")  # {3, 4}
# we also have a syntax sugar for this operation - the - operator
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_7 - num_5_9}")  # {3, 4}
# note that the order matters - if we do num_5_9 - num_3_7, we get different result
num_8_9 = num_5_9.difference(num_3_7)  # {8, 9}
print(f"Difference of {num_5_9} and {num_3_7} is {num_8_9}")  # {8, 9}
# so we can also use the - operator for this operation
print(f"Difference of {num_5_9} and {num_3_7} is {num_5_9 - num_3_7}")  # {8, 9}

# finally we can perform so called symmetric difference - elements that are in one set or the other, but not both
# Latviski symmetric difference - simetriskā atšķirība

num_3_4_8_9 = num_3_7.symmetric_difference(num_5_9)  # {3, 4, 8, 9}
print(f"Symmetric difference of {num_3_7} and {num_5_9} is {num_3_4_8_9}")  # {3, 4, 8, 9}
# we also have a syntax sugar for this operation - the ^ operator
print(f"Symmetric difference of {num_3_7} and {num_5_9} is {num_3_7 ^ num_5_9}")  # {3, 4, 8, 9}
# note that the order does not matter for this operation - it is symmetric


# so to summarize we have 3 major uses for sets
# 1. membership testing - O(1) time complexity
# 2. unique elements - no duplicates allowed
# 3. set operations - union, intersection, difference, symmetric difference
# 3b. set operations - subset, superset, strict subset, strict superset

# looping through sets
for element in unique_foods_set:
    print(element)  # prints each element in the set - order is RANDOM
# note that we cannot use indexing or slicing on sets

# how about numbers from 0 to 9
for n in numbers_0_9:
    print(n)  # prints each number in the set - order is RANDOM