# philosophically while loops are great for times
# when we do not know how long a loop will be

# instead for fixed size loops we use for loops
# for example we have some collection of items or text to loop through

for i in range(5): # range is a sort of number factory 
    print(f"I am number {i}")
    # still inside
    print("Still am", i)
    # we go back to start of for loop until we have nothing left
# now loop ends when there is nothing left to process    
print("Outside i is", i)

# name = "Valdis"
name = "Kaķis"
for c in name:
    print(f"character {c} - Unicode value {ord(c)}")
    
# let's go back to range

# range actually has optionally 3 parameters
# we can have 2 as well start(inclusive) and end (exclusive)

for i in range(10, 15):
    print("printing ", i)
    
print("i is now", i)

for i in range(30, 24, -1): # so last parameter is step here it is negative 1
    print("i is", i)
    
print("outside i is", i)

for i in range(10, 210, 5):
    print(i, end=", ") # we want to print without newlines
    # default print end is newline
    
for n in range(12):
    if n % 2 == 0:
        print("n is even!", n)
    else: # essentially n % 2 == 1
        print("n is odd!", n)
        
import random
# let's throw some dice

# I want to do something 5 times
for _ in range(5): # Python uses _ for variable with no meaning
    print("My dice throw is", random.randint(1,6))
    
    

