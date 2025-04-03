# now how can we combine try and except and while loops to guaranteed
# appropriate input

# try:
#     user_input = input("Please enter an integer!")
#     my_integer = int(user_input)
#     print("Cool we got an int", my_integer)
# except ValueError: # no need for as e unless you need error message
#     print("Sorry, you need to enter an integer!")
#     # for now we would exit
#     exit()

# the big idea is to wrap our try except in a while loop
# we do not know when our users will get smart and enter what we want

while True:
    try:
        user_input = input("Please enter an integer!")
        my_integer = int(user_input) # could throw ValueError
        # here we are sure that we got int
        print("Cool we got an int", my_integer)
        break # now we are safe to break out of this user input loop
    except ValueError: # no need for as e unless you need error message
        print("Sorry, you need to enter an integer!")
        # if i wanted I could use pass instuction here to do nothing
    
# start real work
print(f"Doing some real work with {my_integer}")