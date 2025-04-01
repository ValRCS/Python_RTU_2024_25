# we now talk about Boolean Algebra
# it lets us combine various Boolean values
# let's start with  negation
# unlike most languages which use !
# Python uses English not
is_raining = False
print("Is it raining? ", is_raining)
is_raining = not is_raining # this is like a toggle switch
print("Is it raining? ", is_raining)
is_raining = not is_raining # this is like a toggle switch
print("Is it raining? ", is_raining)
is_raining = not is_raining # this is like a toggle switch
print("Is it raining? ", is_raining)

# double negation gets us back to same value we started with
is_wet = not not is_raining
print("Is it now wet? ", is_wet)


# now let's see conjunction it is True only when BOTH values are True
# Python uses English and for this
# instaed of && used by many other languages
print("True and True", True and True)
print("True and False", True and False)
print("False and True", False and True)
print("False and False", False and False)

if is_raining and is_wet:
    print("Wow so BOTh wet and raining, I should get an umbrella and my shoes!")
else: # this means either it is not wet or not raining or both not raining and not wet
    print("3 choices here")
    print("his means either it is not wet or not raining or both not raining and not wet")
     
# we also have disjunction or logical or
# in Python we use or not || as other languages
print("True or True", True or True)
print("True or False", True or False)
print("False or True", False or True)
print("False or False", False or False)


# i can create longer or or and chains
# only we have to be aware of short-circuit logic
# this means Python will stop the evaluation of logic if it deems
# that statement will be True or False guaranteed
print(False or False or False or 5 > 2 or False or 10/0 )

# similarly one drop of oil can spoin a jar of honey
print(True and 5 > 2 and 2*2 == 4 and 3 < 0 and True and 10/0)

number = 770
if 50 < number < 100: # so this will be true if number is over 50 and less than 100
    print(f"Cool {number} is between 50 and 100!")
else:
    print(f"Cool {number} is either under 50 or equal or 100 or more !")

