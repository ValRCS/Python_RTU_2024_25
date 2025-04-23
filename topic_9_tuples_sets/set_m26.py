# let's talk about set data structure in Python
# Latviski set is - kopa
# set is a collection of unique elements
# set is unordered, unindexed, and mutable

# Some crucial set properties:
# 1. set contains unique elements, meaning that it cannot contain duplicates
# 2. set is unordered, meaning that the order of elements is not guaranteed
# 3. mutable, meaning that you can add or remove elements from a set
# 4. set is iterable, meaning that you can loop through the elements of a set
# 5. can be used for membership testing, meaning that you can check if an element is in a set QUICKLY
# 6. set can be used for mathematical operations like union, intersection, difference, and symmetric difference

# official set documentation: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
# set is a built-in data type in Python, so you don't need to import anything to use it

# we can create sets from all kind of iterables, like lists, tuples, strings, and dictionaries
# we can also create sets from other sets, but the new set will only contain unique elements

# let's start with a string
my_string = "abracadabra maģija mana"
char_set = set(my_string)  # set will contain only unique characters from the string
print(f"String: {my_string}\nSet: {char_set}")

# let's see how many individual characters are in the string
print(f"Number of unique characters in the string: {len(char_set)}")
# let's see how many individual characters are in the string, but we will use a set comprehension

# Major use of sets - membership testing
# we can test for membership in a set using the 'in' keyword 
# this is much faster than testing for membership in a list or a tuple
# this is because sets are implemented using hash tables, 
# which allow for O(1) average time complexity for membership testing
# O(1) means even a large set will be fast to check for membership

needle = "m"
haystack = "abracadabra maģija mana"
# using string membership testing is slower than using set membership testing
print(f"Is '{needle}' in '{haystack}'?") # this will need to check each character in the string
print(f"Using string: {needle in haystack}") # this will need to check each character in the string
print(f"Using set from scratch: {needle in set(haystack)}") # this will need to check each character in the string
# above is not very useful, because we are creating a set from scratch each time we need to check for membership
# note however that we do not gain anything by making set from scratch each time we need to check for membership
# so it would be actually useful to use existing set for membership testing
print(f"Using existing set: {needle in char_set}") # this will need to check each character in the string

# so this means if If I expect to check multiple times for membership in some collection of elements,
# then it might make sense to create a set from that collection of elements first
# and then use that set for membership testing

# how about set from list
foods = ["apple", "banana", "orange", "kiwi", "apple", "banana"]
food_set = set(foods)  # set will contain only unique elements from the list
print(f"List: {foods}\nSet: {food_set}") # again ORDER IS NOT GUARANTEED!

# if I want them orderd then I can simply use sorted() function to get a list
sorted_foods = sorted(food_set)  # this will sort the set and return a list
# if I did not care about order then I could use list() function to get a list
unique_food_list = list(food_set)  # this will convert the set to a list, but the order is not guaranteed
print(f"Sorted list: {sorted_foods}") # this will sort the set and return a list
print(f"Unique list: {unique_food_list}") # this will convert the set to a list, but the order is not guaranteed

# so recipe for creating unique list from a list is:
# 1. create a set from the list to remove duplicates
# 2. use sorted() function to sort the set and return a list or use list() function to convert the set to a list
also_unique_food_list = list(set(foods))  # this will convert the set to a list, but the order is not guaranteed
print(f"Unique list: {also_unique_food_list}") # this will convert the set to a list, but the order is not guaranteed

# so let's mutate the set by adding and removing elements
# let's add mango to the set
food_set.add("mango")  # this will add mango to the set
print(f"Set after adding mango: {food_set}") # this will add mango to the set
# how about kiwi again?
food_set.add("kiwi")  # this will not add kiwi to the set, because it is already in the set
print(f"Set after adding kiwi again: {food_set}") # this will not add kiwi to the set, because it is already in the set

# let's remove banana from the set
food_set.remove("banana")  # this will remove banana from the set
print(f"Set after removing banana: {food_set}") # this will remove banana from the set
# remove raises KeyError if the element is not in the set
try:
    food_set.remove("banana")  # this will raise KeyError, because banana is not in the set
except KeyError as e:
    print(f"KeyError: {e}")

# we could also check first using in keyword if the element is in the set
if "banana" in food_set:
    food_set.remove("banana")  # this will remove banana from the set
    print(f"Set after removing banana: {food_set}") # this will remove banana from the set
else:
    print(f"banana is not in the set, so we cannot remove it")

# instead if you do not care if the element is in the set or not, you can use discard() method
# this will not raise KeyError if the element is not in the set
food_set.discard("banana")  # this will not raise KeyError, because banana is not in the set
print(f"Set after discarding banana: {food_set}") # this will not raise KeyError, because banana is not in the set

# now let's talk about set operations
numbers_0_11 = set(range(12))  # this will create a set of numbers from 0 to 11
num_3_7 = set(range(3, 8))  # this will create a set of numbers from 3 to 7
num_5_9 = set(range(5, 10))  # this will create a set of numbers from 5 to 9

print(f"numbers_0_11: {numbers_0_11}")  # this will create a set of numbers from 0 to 11
print(f"num_3_7: {num_3_7}")  # this will create a set of numbers from 3 to 7
print(f"num_5_9: {num_5_9}")  # this will create a set of numbers from 5 to 9

# first let's check subset and superset
# subset is a set that contains only elements that are in another set
# superset is a set that contains all elements of another set

# so let's check if num_3_7 is a subset of numbers_0_11
print(f"Is num_3_7 a subset of numbers_0_11? {num_3_7.issubset(numbers_0_11)}")  # this will check if num_3_7 is a subset of numbers_0_11
# Python offers us syntactic sugar for this, we can use <= operator to check if one set is a subset of another set
print(f"Is num_3_7 a subset of numbers_0_11? {num_3_7 <= numbers_0_11}")  # this will check if num_3_7 is a subset of numbers_0_11
# we also have strict subset, which means that the two sets are not equal
# we can use < operator to check if one set is a strict subset of another set
print(f"Is num_3_7 a strict subset of numbers_0_11? {num_3_7 < numbers_0_11}")  # this will check if num_3_7 is a strict subset of numbers_0_11
# so let's check if set is subst of itself
print(f"Is num_3_7 a subset of itself? {num_3_7 <= num_3_7 }")  # this will check if num_3_7 is a subset of itself
# this will also check if num_3_7 is a strict subset of itself
print(f"Is num_3_7 a strict subset of itself? {num_3_7 < num_3_7}")  # this will check if num_3_7 is a strict subset of itself

# of course I can check for equality of two sets using == operator
# this will check if num_3_7 is equal to numbers_0_11
print(f"Is num_3_7 equal to numbers_0_11? {num_3_7 == numbers_0_11}")  # this will check if num_3_7 is equal to numbers_0_11
# this will check if num_3_7 is equal to itself
print(f"Is num_3_7 equal to itself? {num_3_7 == num_3_7}")  # this will check if num_3_7 is equal to itself

# similarly we can go the other way around and check if numbers_0_11 is a superset of num_3_7
# this will check if numbers_0_11 is a superset of num_3_7
print(f"Is numbers_0_11 a superset of num_3_7? {numbers_0_11.issuperset(num_3_7)}")  # this will check if numbers_0_11 is a superset of num_3_7
# we cna use >= operator to check if one set is a superset of another set
print(f"Is numbers_0_11 a superset of num_3_7? {numbers_0_11 >= num_3_7}")  # this will check if numbers_0_11 is a superset of num_3_7
# this will check if numbers_0_11 is a strict superset of num_3_7
print(f"Is numbers_0_11 a strict superset of num_3_7? {numbers_0_11 > num_3_7}")  # this will check if numbers_0_11 is a strict superset of num_3_7

# so let's use union operation to combine two sets
# union is a set that contains all elements that are in either set
num_3_9 = num_3_7.union(num_5_9)  # this will create a set of numbers from 3 to 9
print(f"num_3_9: {num_3_9}")  # this will create a set of numbers from 3 to 9
# we also have syntactic sugar for this, we can use | operator to combine two sets
print(f"num_3_7 | num_5_9: {num_3_7 | num_5_9}")  # this will create a set of numbers from 3 to 9
# this reminds us of || use for or in other languages, like C, C++, Java, etc.

# there is a tiny difference between union and | operator
# with | operato we NEED to have both sets defined before we can use it
# with union we can use it on one set and pass any iterable to it such as list, tuple, set, etc.

# now let's use intersection operation to combine two sets
# intersection is a set that contains all elements that are in both sets
num_5_7 = num_3_7.intersection(num_5_9)  # this will create a set of numbers from 5 to 7
print(f"num_5_7: {num_5_7}")  # this will create a set of numbers from 5 to 7
# we also have syntactic sugar for this, we can use & operator to combine two sets
# again & reminds us of && use for and in other languages, like C, C++, Java, etc.
print(f"num_3_7 & num_5_9: {num_3_7 & num_5_9}")  # this will create a set of numbers from 5 to 7

# now we only have left difference and symmetric difference
# so difference is a set that contains all elements that are in one set but not in the other set

num_3_4 = num_3_7.difference(num_5_9)  # this will create a set of numbers from 3 to 4
print(f"num_3_4: {num_3_4}")  # this will create a set of numbers from 3 to 4
# again we have syntactic sugar for this, we can use - operator to combine two sets
print(f"num_5_9 - num_3_7: {num_5_9 - num_3_7}")  # this will create a set of numbers from 5 to 9
# this will create a set of numbers from 5 to 9 that are not in num_3_7

# finally we have symmetric difference
# symmetric difference is a set that contains all elements that are in one set or the other set but not both
# this is like xor operation in other languages, like C, C++, Java, etc.
num_3_4_8_9 = num_3_7.symmetric_difference(num_5_9)  # this will create a set of numbers from 3 to 4 and 8 to 9
print(f"num_3_4_8_9: {num_3_4_8_9}")  # this will create a set of numbers from 3 to 4 and 8 to 9

# we could have used ^ operator to do the same thing
print(f"num_3_7 ^ num_5_9: {num_3_7 ^ num_5_9}")  # this will create a set of numbers from 3 to 4 and 8 to 9

# note that symmetrical difference is same as union of of two set differences
print(f"num_3_7 - num_5_9 | num_5_9 - num_3_7: {num_3_7 - num_5_9 | num_5_9 - num_3_7}")  # this will create a set of numbers from 3 to 4 and 8 to 9

# Conclusion
# Use sets for membership testing, removing duplicates, and set mathematical operations

# Typical use cases for sets:
# 1. Removing duplicates from a list or a tuple
# 2. Checking for membership in a collection of elements

# how about some practical examples of set operations
# let's say we have two lists of students, one for each class
# and we want to find out which students are in both classes, or which students are in either class
# or which students are in one class but not the other class
class_a = ["John", "Mary", "Peter", "Paul", "Anna"]
class_b = ["Mary", "Paul", "George", "Anna", "Tom"]
# let's create sets from the lists
class_a_set = set(class_a)  # this will create a set of students in class A
class_b_set = set(class_b)  # this will create a set of students in class B
# now we can use set operations to find out which students are in both classes, or which students are in either class
print(f"Students in both classes: {class_a_set.intersection(class_b_set)}")  # this will create a set of students in both classes
print(f"Students in either class: {class_a_set.union(class_b_set)}")  # this will create a set of students in either class
print(f"Students in class A but not in class B: {class_a_set.difference(class_b_set)}")  # this will create a set of students in class A but not in class B
print(f"Students in class B but not in class A: {class_b_set.difference(class_a_set)}")  # this will create a set of students in class B but not in class A