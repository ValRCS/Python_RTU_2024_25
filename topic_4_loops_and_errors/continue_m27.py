# we have a bit rare command
# continue it goes to START of loop immediately

i = 0
while i < 15:
    print("i is", i)
    if i == 3:
        print("Special case i is ", i)
        i += 5 # big jump
        continue # now we jump to start of loop
    # if you think about it we could have done this without continue
    # we simply had to put the following code in else:
    print("normal case", i)
    i += 1
    # back to start of loop
print("i should be 15 now", i)