# Boolean Algebra
# Booleans are named after George Boole who invente Boolean Algebra
# negation
is_raining = False
print("Is it raining?", is_raining)
is_raining = not is_raining # so called toggle construction
# note that in Python we used English not , not ! as in most  other languages
print("Is it raining?", is_raining)
is_raining = not is_raining # so called toggle construction
print("Is it raining?", is_raining)
is_raining = not is_raining # so called toggle construction
print("Is it raining?", is_raining)

# conjuction so only when BOTH sides are True!
# we use English and , not && as in other langauges
print("True and True ?", True and True)
print("True and False ?", True and False)
print("False and True ?", False and True)
print("False and False ?", False and False)

have_umbrella = True
if is_raining and have_umbrella:
    print("Whew I can take an umbrella and go outside in RAIN")
else:
    print("3 possibilities here")
    print("Either I do not umbrella or it is not raining")
    print("Or possibly it is not raining AND I have no umbrella")
    
# with disjunction only one side has to be True
# again we use English or, not || as in other languages
print("True or True ?", True or True)
print("True or False ?", True or False)
print("False or True ?", False or True)
print("False or False ?", False or False)

# we can have longer chains of logic
# just note that we have short-circuit logic
# this means that chain will stop the moment Python knows the value!
print(False or False or False or False or True or False or 5/0)
# 5/0 will not run because True came before

# similary with and chain one False value will stop the chain and produce False
print(True and 5 > 4 and 10 > 8 and 2 > 3 and 56/0) # again 56/0 will not run

# finally Python offers us a nice way to compare multiple values
number = 41
print("Is number between 30 and 70?", 30 < number < 70)
# in other languages we would write the same thing thusly
print(f"Is {number} between 30 and 70?", 30 < number and number < 70)

# we can use this in if of course
if 30 < number < 70:
    print("Nice the number is between 30 and 70 exclusive [30,number,70]")
else:
    print("number is either 30 or less or 70 or more")




