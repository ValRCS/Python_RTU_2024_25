# let's try to save some data while running a Python program
print("Starting our program")
# in Python we can make a new variable at any time
# we simply use = to assign some value / reference
name = "Valdis" # variable name refers to string "Valdis"
print(name)
# compare with string literal
print("name")
# in Python we start our variables with lowercase or uppercase letter
# we can use _ for longer variables or to start
# we can use numbers in variables but not at start
name2 = "Pēteris" # in general name2 is not a good name for variable
print(name2)

# our variables should show meaning

print(name, "and", name2, "are friends.")
sentence = name + " and " + name2 + " are friends."
# there is easier f-strings syntax for longer string creation
print(sentence)

# variable names should provide meaning
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
seconds_this_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year
print(seconds_this_year)

# we talked about f-strings for formatting text
print(f"This year has {seconds_this_year} seconds")
# what about without f? we simply print then exactly no variables
print("This year has {seconds_this_year} seconds")

# i could have saved it of course
seconds_string = f"This year has {seconds_this_year} seconds"
print(seconds_string)

# f-strings allow you to even evaluate arithmetic inside
math_result = f"Soo 2*2={2*2}"
print(math_result)

# so recommendations for variables
# use short variables but at the same time understandable
# a is not a great name unless a has some meaning
# x, y, z are good names for coordinate variables
# t could be time or temporary
# i, j are used for loops, iteration, we will look at loop soon
# c could be character - technically Python only has strings

# do not use non english characters in variables
# kaķis = "Vinnijs" # legal, but AVOID! english letters only
# print(kaķis)

# instead use
cat_name = "Dārcijs"
print(f"My other cat is {cat_name}")
print(f"Variable cat_name: {cat_name} is of data type {type(cat_name)}")

# Python is very liberal it lets us change values whenever we need
cat_name = 5000 # allowed even though a bit confusing...
# we changed our data type from str to int
print(f"Now my cat is {cat_name}")

# i can print the data types of my variables
print(type(cat_name))
print(f"Variable {cat_name} is of data type {type(cat_name)}")

MY_PI = 3.1415926
print(f"MY PI is {MY_PI} and its type is {type(MY_PI)}")

# we can change data types - called casting
American_PI = int(MY_PI) #HERE we lose all after comma
print(f"American PI is {American_PI} and its type {type(American_PI)}")

# how about going back what will happen?
floating_pi = float(American_PI)
print(f"floating_pi is {floating_pi} and its type will be {type(floating_pi)}")