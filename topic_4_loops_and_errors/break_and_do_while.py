# some languages have another type of loop
# so called do while loop
# I call it
# "shoot first and ask questions later"
# the condition is AFTER the loop is done at least once
# Python does not have it, but has an easy way to emulate this

# i = 0
i = 9_000
while True:
    print("Doing something with i", i) # this instruction will run at least once!
    i += 1
    if i > 5:
        print("Time to get out and break freeee")
        break # break leaves the inner most loop immediately
    print("I could do more with i here", i) #back to while True
print("I am outside and i is", i)

# we would ask for user input using break again
total = 0
while True:
    print(f"Total so far: {total}")
    user_input = input("Enter number or letter q to quit")
    if user_input == "q":
        print("Quitting time today!")
        break # leave the loop
    n = float(user_input)
    total += n
    # i could other checks and other breaks
    
print(f"Outside total is {total}")