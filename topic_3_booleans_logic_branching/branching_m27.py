# major use of Booleans is to branch
# this means we tell computer which command(s) to run
# conditionally
is_warm = True
# is_warm = False
# we can check for boolean and do something
if is_warm:
    print("Let me go swimming!")
    print("Let me get a margarita!")
    # we are still inside the if branch

# we are done with the if above
# this is just normal code
print("I am sleeping like usual")

current_temp = 15 + 20
hot_temp = 25

if current_temp < hot_temp:
    print("It is not so hot")
    print(f"Current temperature is {current_temp} which is less than {hot_temp}")
else: # we hit this branch if current_temp >= hot_temp
    print("Oh quite toasty!")
    print(f"Current temperature is {current_temp} which is more or equal than {hot_temp}")
    
secret_number = 42
guess = 55
# guess = int(input("Try to guess my number -> "))

if guess > secret_number:
    print(f"Your guess {guess} is too high")
elif guess < secret_number: # if first if is False (guess is not over secret_number)
    print(f"Your guess {guess} is too low.....")
else: # means above if and elif were false
    # this means guess == secret_number
    print(f"Cool you guessed {guess} that is my {secret_number} !")
    
    
# we can also nest if's inside other ifs and so on
# just beware the nested if hellll


# a = 10_000 # same as 10000 we can use _ to visually emphasize numbers
a = 1_000_000
if a < 100:
    print("a is less than 100", a)
    # we can now nest inside this if
    if a < 50:
        print("a is less than 50 actually", a)
    else: # means a >= 50 and a < 100 still
        print("a is between 50 included and 100 excluded", a)
else: # means a >= 100
    print("a is 100 or more")
    if a > 9000:
        print("A is over 9000!", a)
    else:
        print("a is 9000 or less", a)