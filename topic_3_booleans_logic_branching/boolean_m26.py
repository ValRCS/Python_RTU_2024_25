# let's learn a new data type - Booleans
# essentially that is True or False
# 1 or 0, yes or no, red or black
# Booleans are our most basic building blocks in programming
is_warm = True # in Python note the capitalization for True
is_sunny = False #
# Now let's print them out
print("Is it warm?", is_warm)
print(f"Is it sunny out? {is_sunny}")

# the data type
print(f"The data type of {is_warm} is {type(is_warm)}")

# how else can we get Booleans
# we can get them by comparison operators
print(2 > 3)
print(2 < 3)
print(f"Is 2 > 3? {2 > 3}")
# we can save results of comparison
alice_age = 20
bob_age = 35
is_alice_older_than_bob = alice_age > bob_age
print(f"Is Alice {alice_age} older than Bob {bob_age}? {is_alice_older_than_bob}")

# we have less or equal
# and we have greater or equal
a = 2
b = 4
c = 5
print(f"Is {a}*{a} <= {b}? {a*a <= b}")
print(f"Is {a}*{a} >= {b}? {a*a >= b}")
print(f"Is {a}*{a} <= {c}? {a*a <= c}")
print(f"Is {a}*{a} >= {c}? {a*a >= c}")

# we have equality comparison
print(f"Is {a}*{a} == {b}? {a*a == b}")

# we also have inequality operator !=
print(f"Is {a}*{a} != {b}? {a*a != b}")
print(f"Is {a}*{a} != {c}? {a*a != c}")

# we have to be a bit careful when comparing floats
# we can compare with > or < that is fine
# exact comparison for equality with == might not work as expected
# due to the way floats are represented
# we can compare to some digits after round
d = 0.1 + 0.2 # this will not be 0.3 !!!
e = 0.3
print(f"is {d} equal to {e} ? {d == e}")
# we could round at some point
precision = 2
print(f"is {d} equal to {e} ? {round(d, precision) == round(e, precision)}")
# we can compare their difference to some

# we can compare int and float also

# we can compare strings
name =    "Valdis"
garais =  "Valdiss"
latvian = "Vāldis"
buddy =   "Voldemārs"

print(f"Is {name} < {buddy} ? {name < buddy} ")
print(f"Unicode for a is {ord('a')}")
print(f"Unicode for o is {ord('o')}")

print(f"Is {name} < {garais} ? {name < garais} ")

print(f"Is {buddy} < {latvian} ? {buddy < latvian} ")
print(f"Unicode for ā is {ord('ā')}")

# finally how about length?
name_len = len(name)
buddy_len = len(buddy)
print(f"Number of letters in {name} is {name_len}")
print(f"Number of letters in {buddy} is {buddy_len}")
print(f"Thus does {name} is SHORTER than {buddy}? {name_len < buddy_len} ")