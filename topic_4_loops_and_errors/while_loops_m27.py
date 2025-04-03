# print("Alice did")
# print("talk")
# print("talk")
# print("talk")
# how about 100 times or 1_000_000 times?
# 
# print("Alice is")
# 
# # we have a new construction
# # while loop does something while its condition is True
# while True: # note again colon means indentation for inner block
#     print("dancing")
#     print("singing")
#     print("talking")
# 
# # will we reach line 17?
# print("she is done...")

# infinite loops can be useful as main loops in application
# provided there is some means of escape..

# other use is to use some sort of loop variable - iterator, counter

i = 0 # very typical to call loop variable i, could be it, or j
while i < 4: # if False go to the next line after indented block
    print("i is ", i)
    print(f"Still inside loop and i is {i}")
    # we need to change the loop variable somehow
    # typical would be to increase by 1
    i += 1 # this is same as i = i + 1
    # here we go back to the start of loop
# here the while loop exits when False    
print(f"When loop is done the value of i is {i}")

floor = 9
while floor >= 0:
    print(f"Going down on floor {floor}")
    floor -= 1 # same as floor = floor - 1
print(f"Whew I am outside on floor {floor}")

# we can use any type of operation
# we could add larger or smaller numbers
# we could multiply or do anything
# or we could use a flag approach

# product = 1
# while product < 100:
#     print(f"Patlaban product ir {product}")
#     num = int(input("Ievadiet veselu skaitli")) # TODO reminder to show error checking
#     product *= num # same as product = product * num
# print(f"Outside loop the product is {product}")
# 
# again while loop by its nature is indeterminate

# it is easy to make larger steps
start = 10
end = 30
step = 2
i = start # critical to not skip this line if we are reusing our variables
while i < end:
    print(f"Doing something with i {i}")
    i += step
print(f"Outside the loop the value is i {i}")
# note there is a better way to loop through specific numbers with for loops


# another tool or approach is use of flags to control our loop
is_job_active = True
job_count = 0
MAX_JOBS = 10
while is_job_active and job_count < MAX_JOBS:
    print(f"Doing something Job No. {job_count}")
    job_count += 1 # Python does not have ++ operator which is same as += 1
    user_input = input("is job done? enter y to finish")
    if user_input == "y": # for better UX would be to allow Y and other inputs to quit
        is_job_active = False
    # now we go back to start and check our flag
    
print("jobs done", job_count)