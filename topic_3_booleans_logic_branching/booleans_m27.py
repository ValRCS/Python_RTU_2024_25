# let's talk about a new data type - Boolean
# it only takes on two values - True or False
# in other words 1 or 0, yes or no, red or black, on or off
# Booleans are the basic building block of programs
is_foggy = False # Python automatically assigns the correct data type
is_warm = True
print("Is it foggy outside?", is_foggy)
print("Is it warm outside?", is_warm)

# if we want we can check the data type
print(f"The data is {is_foggy} and its type is {type(is_foggy)}")

# we typically get Booleans by comparison operators
print(5 < 10)

# we can save the results of our boolean
is_math_good = 2*2 < 5
print("Is math still good?", is_math_good)

a = 2  
b = 4
c = 5

print(f"{a}*{b} > {c} ? ", a*b > c)

# we also have less than or equal
# and also greater than or equal
print("2*2 >= 4 ?", 2*2 >= 4)
print("a*b >= c ?", a*b >= c)

# similarly we have less than or equal
print("2*2 <= 4 ?", 2*2 <= 4)
print("a*b <= c ?", a*b <= c)

# then we have equality, in Python we use ==
print("2*2 == 4 ?", 2*2 == 4)
print("2*2 == 5 ?", 2*2 == 5)

# then we have inequality with !=
print("2*2 != 4 ?", 2*2 != 4)
print("2*2 != 5 ?", 2*2 != 5)

# we can compare floats but careful with equality comparison

d = 0.1 + 0.2 # this is 0.3000000005 in float
e = 0.3
print(f"is {d} equal to {e}?", d == e) # will be False
# we could round the values
precision = 2
print(f"is {d} roughly equal to {e}?", round(d, precision) == round(e, precision))

name = "Valdis"
friend = "Voldemārs"

print(f"Is {name} < {friend}?", name < friend)

short_friend = "Vold"
print(f"Is {name} < {short_friend}?", name < short_friend)

print(f"Unicode for a is", ord("a"))
print(f"Unicode for o is", ord("o"))

tall_friend = "Vāldis"
print(f"Is {tall_friend} < {friend}?", tall_friend < friend)

print(f"Unicode for ā is", ord("ā"))
print(f"Unicode for Ķ is", ord("Ķ"))

# if we know the unicode number for symbol we can print
print(f"Let's print character number 290 in Unicode", chr(290))

# back to comparison
# if we want to compare by string length
name_len = len(name)
friend_len = len(friend)
print(f"Name {name} has less characters than {friend} ?", name_len < friend_len)
print(f"{name} has {name_len} characters")
print(f"{friend} has {friend_len} characters")

# we also have membership checks with in operator
print("is 'al' in Valdis ? ", 'al' in name)
print("is 'alus' in Valdis ? ", 'alus' in name)

# there is also is operator
# which checks whether variables refer to same object in memory


