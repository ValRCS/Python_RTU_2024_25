# print("Alice did")
# print("talk")
# print("talk")
# print("talk")
# 
# # how much copy and pasting can we tolerate?
# 
# while True: # while something is True do the following
#     print("dance")
#     print("read")
#     print("talk")

# will we ever reach this?
# print("Alice is now outside")

# instead of True let's consider some condition that can change
i = 0
while i < 4: # if this is False then we go to line outside of our loop
    print(f"value of i is {i}")
    # we need to change the value of i to reach the end of loop
    i += 1 # same as i = i + 1 # we increment i by 1
    # Python does not have ++ operation
    # here the loop goes back to beginning and check the while condition i < 4
    print("Still inside and i is", i)
# this is where we end up if i < 4 is False    
print("We are outside of loop!")

floor = 9
while floor >= 0:
    print(f"Going down in an elevator on floor: {floor}")
#     floor -= 1 # so same as floor = floor - 1
    # we can take a fast elevator
    floor -= 2
    
print(f"Whew I am out of elevator on floor {floor}")

keep_looping = True
total = 0
while keep_looping:
    user_input = input("input a number to add or q to exit")
    if user_input == "q":
        keep_looping = False
    else:
        number = float(user_input)
        total += number
        print(f"Total after adding {number} is {total}")
    
print("We are outside and total is", total)

# instead of flags we can also use a break command to leave loop early

while True:
    user_input = input("input a number to add or q to exit")
    if user_input == "q":
        print("I see you do not want to continue this loop. Ok let's break out!")
        break # leave current loop immediately
    print(f"Doing something with user input {user_input}")
    # with this approach we get a bit flatter code without else
    
print("Free of loops again!") # this is where we go after break

# we have another helper command called continue
# continue goes to the beginning of loop

i = 0
while i < 10:
    print("We got i", i)
    if i % 2 == 0:
        print("Cool you got an even number!", i)
        i += 1
        continue # we go to the beginning of loop
    # instead of continue we could have used else:
    print("We have an odd number!", i)
    i += 1

