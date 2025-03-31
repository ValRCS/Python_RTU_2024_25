# we can use booleans to branch
# this means we can choose which commands will run
# on some condition
is_warm = True
# is_warm = False
# we can check for boolean and then do something conditionally
if is_warm:
    print("Let's go out for a walk it must be nice!")
# here we are out of the if
# this is main block and will always runZ
print("We will go out anyway")

temperature = 20.5 - 5
if temperature > 20:
    print(f"Nice temperature is over 20 actually {temperature} so we are happy!")
    print("Let's go play")
    # we keep writing what we want to do when t > 20
else: # this means temperature is 20 or less
    print("hmm I might want to grab a jacket")
    print("And only then go out")
    # we can keep going here for those instructions when t<= 20
# now we are outside if else block
print("I am outside!!")

# if we have 3 roads and we want to exactly one
# we can use if elif else block
# here order of comparisons is important!

secret_number = 42
guess = 540
# guess = int(input("Please enter an integer!"))

if guess > secret_number:
    print(f"your guess {guess} is more than secret")
elif guess < secret_number: # this branch will not be checked at all if first branch is True!
    print(f"your guess {guess} is less than secret")
else: # if impossible is removed, then only improbable remains, here this means 42
    print(f"Cool you found my secret {secret_number} just like yours {guess}")
    
# we can have if inside another if and so on
# so called nested ifs
a = 10
if a < 100:
    print("a is less than 100", a)
    if a < 50:
        print("Actually is less than 50!", a)
    else: # so 50 <= a < 100
        print("So a is 50 or more but less than 100!")
else:
    print("a is at least hundred",a)
    
if a >= 100:
    print("a is at least hundred",a)
elif a >= 50:
    print("So a is 50 or more but less than 100!")
else: # only values less than 50 remain
    print("Actually is less than 50!", a)