# so for loops are for looping through SOME collection of items
# Python has many different iterable collections
# we can even make our own

# basic for loop using range to print some numbers
# range(5) will give you numbers 0,1,2,3,4 on demand
for i in range(5): # range is iterable that gives you numbers on demand
    print(f"I am number {i}")
    
print("Outside At end the number is", i)

j = 0
while j < 5:
    print(f"j is now {j}")
    j += 1
print("outside loop j is", j)

# we can loop through strings with for loop
name = "Valdis"
for char in name: # could use c, or it, or item, element etc
    print("Current char is", char)
    
# let's print numbers 10 until 15
for n in range(10,16): # so last item is not included
    print("n:", n)
    
# we can get step
for n in range(100,111,5): # so 3rd parameter is step
    print("n is", n)
    
# we can go down
for floor in range(9,-2,-4):
    print("On floor", floor)
print("Outside on floor", floor)
    
    