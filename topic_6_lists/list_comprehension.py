# it is typical to create a list using a for loop
# we start with an empty list then do some operations

numbers = list(range(12)) # so 0 to 11
print(numbers)

# so to create squares i would do this
squares = [] # empty list
for n in numbers:
    squares.append(n ** 2) # append the square of n to the list
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

# Python offers an alternative way of creating such a list
# it is called a list comprehension
# syntax is:
# [expression for item in iterable if condition]
# so we can do this in one line
also_squares = [n ** 2 for n in numbers] # this is a list comprehension
print(also_squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

# we could also use this for more complicated cases by combinint it with if statements
# let's create odd squares the standard way
odd_squares = [] # empty list
for n in numbers:
    if n % 2 == 1: # odd number
        odd_squares.append(n ** 2) # append the square of n to the list
print(odd_squares) # [1, 9, 25, 49, 81, 121 ]

# list comprehension for odd squares
odd_squares_comp = [n ** 2 for n in numbers if n % 2 == 1] # this is a list comprehension
print(odd_squares_comp) # [1, 9, 25, 49, 81, 121]

# when to use list comprehensions?
# when the logic is simple and easy to read