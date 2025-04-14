# We saw how often we create new lists from existing lists using for loops.
# This is a common pattern in Python, and it's often done using list comprehensions.

# let's see a classical approach

numbers = list(range(12)) # from 0 to 11 inclusive
print("Numbers:", numbers)

# let's make a new list of squares of the numbers
squares = [] # empty list to hold the squares
for number in numbers: # numbers is just a name for item, could be n or x or anything else
    squares.append(number ** 2) # append the square of the number to the list
print("Squares:", squares)

# Python offers a more concise way to do this using list comprehensions.
# list comprehensions are a way to create lists in a single line of code.
# syntax:
# [expression for item in iterable if condition]
# where expression is the value to add to the list, item is the variable name for each item in the iterable,

also_squares = [number ** 2 for number in numbers] # same as above but in one line
print("Also squares:", also_squares)

# this is not all we could filter 
# let's say we want to get squares from only odd numbers

# classical approach
odd_squares = [] # empty list to hold the squares
for number in numbers:
    if number % 2 == 1: # check if the number is odd
        odd_squares.append(number ** 2) # append the square of the number to the list

print("Odd squares:", odd_squares)

# same thing with list comprehension
also_odd_squares = [number ** 2 for number in numbers if number % 2 == 1] # same as above but in one line
print("Also odd squares:", also_odd_squares)

# now the 1000 dollar question: when to use which?

# list comprehensions are more readable and concise, but they can be less clear for complex operations.

# so if you have complicated logic, it's better to use a for loop.
# if you have simple logic, it's better to use a list comprehension.

# note also with classical approach
# we could created odd squares and even squares in one go
# but with list comprehension we would need to create two separate comprehensions
# so in this case it's better to use a for loop

# example
odd_squares = [] # empty list to hold the squares I overwrite the old one!
even_squares = [] # empty list to hold the squares
for number in numbers:
    if number % 2 == 1: # check if the number is odd
        odd_squares.append(number ** 2) # append the square of the number to the list
    else:
        even_squares.append(number ** 2) # append the square of the number to the list

print("Odd squares:", odd_squares)
print("Even squares:", even_squares)