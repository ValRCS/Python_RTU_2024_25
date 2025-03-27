# generally we have some data we want to use multiple times in a program
# for that it is very handy to have variables
print("Let's start a program")
# print(name) # here this will be an error! not yet defined
name = "Valdis" # in Python variables are declared when we use them
print(name)
# compare with string "name" which is just some text not variable!
print("name")
print(f"Hello, my name is {name}, nice to meet you!")
friend = "Pēteris"
print(f"Friend of {name} is {friend}")
# without f strings I could do this
print("Friend of " + name + " is " + friend)
greeting = f"Hello, I am {name}, nice to meet you!"
print(greeting)

# variables start with lowercase or uppercase alphanumeric
# use only English letters
# afterwards we can add digits and also underscore _
# it is good practice to separate words with _

seconds_in_minute = 60 # in real life I would probably use just seconds as variable name
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
seconds_in_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year
print(seconds_in_year)

# there are some common short names
# t is for time or temporary
# s could be for string temporary
# i, j will be used to count and iterate in loops
# c could be character even though Python only has strings
# a,b,c could be used for short code examples but should be avoided for longer code
# good ones are x,y,z if we are dealing with coordinates

# you can show data types when running some code
print(f"Value of name is {name} and its data type is {type(name)}")
# technically Python lets you reassign to anything
# so we can change our data type automatically
name = 7
print(f"Value of name is {name} and its data type is {type(name)}")
# i do not want to be number
name = "Valdis" # of course name could be anything else else
print(f"Whew I am back to good old {name}")



