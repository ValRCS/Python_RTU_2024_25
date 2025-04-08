print("Hello string world!")
# So what are strings after all?
# Strings are a sequence of characters. They can be letters, numbers, symbols, or even whitespace.
# Python does not have a char type. Instead, it uses strings to represent characters.
# Even a single character is a string in Python.
# Strings are immutable, meaning they cannot be changed after they are created.
# We can however overwrite the variable with a new string.

# Kas ir string datu tips?
# String datu tips ir datu tips, kas satur simbolus, burtus un ciparus.

# Let's start with some healthy food example
food = "apple"
# Let's print the food variable
print(food)
# Let's print the type of the food variable
print(type(food))
# Let's print the length of the food variable
print(f"My food {food} has {len(food)} characters")
# In Python there is no difference between single and double quotes
drink = 'kefīrs'
# Let's print the drink variable
print(drink)

# when can it be useful to use single and double quotes?
# When you want to include a quote in the string without escaping it.
# for example:
print("Alice said: 'Hello!'")
print('Alice said: "Hello!"')

# sooo what do we do when we need BOTH quotes in the string?
# We can use triple quotes for that. Triple quotes can be either single or double quotes.
# Triple quotes are also used for multi-line strings.
multi_line_string = """This is a multi-line string.
    It can span multiple lines.
It can also contain 'single' and "double" quotes.
"""
print(multi_line_string)
# similarly I could have used single quotes for the triple quotes

# even better I can use triple quotes with f-strings
name = "Alice"
age = 30
# Let's print the name and age variables using f-strings in multi-line string
big_greeting = f"""Hello {name}!
    You are {age} years old.
    Welcome to the string world!
"""
print(big_greeting)

# we also could have used so called escape characters to include quotes in the string
escaped_text = 'This is a string with an escaped quote: \'Hello!\''
print(escaped_text)
# there are a number of characters we can escape in Python strings:
# \n - new line
# \t - tab
# \\ - backslash means we get a single backslash in the string
# \' - single quote means we get a single quote in the string
# \" - double quote means we get a double quote in the string
# the following are much more rarely used:
# \r - carriage return (moves the cursor to the beginning of the line)
# \b - backspace (deletes the previous character)
# \f - form feed (moves the cursor to the next line)
# \a - bell (makes a sound)
# \v - vertical tab (moves the cursor down one line)
# full list of escape characters can be found here: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

# let's use the common ones in a single string
# and print it out
escaped_string = "This is a string with an escaped quote: \'Hello!\'\nAnd this is a new line.\t\t\tAnd this is a tab."
print(escaped_string)

# now let's talk about indexing in Python
# we use indexing to access individual characters in a string
# indexing starts at 0 in Python
# so the first character in the string is at index 0

name = "Valdis"
# Let's print the first character in the name variable
print(name[0])
# let's print the second character in the name variable
print(name[1]) # so 2nd character has index 1

# let's get length of the string
name_len = len(name)
print(f"Length of the string {name} is {name_len}")
# this means that the last character would have index name_len - 1 that is 5
print(name[5])
# more importantly in general this could be done for any string
print(name[len(name) - 1]) # again this is the last character in the string
# above is not Pythonic way to do it
# instead we can use negative indexing
# negative indexing starts at -1 for the last character in the string
# and goes to -n for the first character in the string
# so the last character in the string is at index -1
print(name[-1]) # this is the last character in the string
# now second to last character is at index -2
print(name[-2]) # this is the second to last character in the string

# let's get some alphabetical characters from the string
alphabet = "abcdefghijklmnopqrstuvwxyz"
# let's make sure we got 26 characters in the string
print(f"Length of the string {alphabet} is {len(alphabet)}")
# so to get letter g which is 7th letter in the alphabet we can use index 6
print(alphabet[6])
# how about 3rd from the end? that would be index -3
print(alphabet[-3])

# so what happens if I exceed my bounds for index
try:
    print(alphabet[26]) # this will raise an error because this refers to 27th character in the string
except IndexError as e:
    print(f"IndexError: {e}")

# -26 would work
print(alphabet[-26]) # this is the first character in the string
# -27 would raise an error
try:
    print(alphabet[-27]) # this will raise an error because this refers to 27th character in the string
except IndexError as e:
    print(f"IndexError: {e}")

# so now we know how to acces individual characters in the string
# how about getting longer substrings from the string?
# in Python we call this slicing
# slicing is done using the following syntax: string[start:end:step]
# note end is not included in the slice!

# so let's start with getting first 3 characters from the string
print(f"First 3 characters in the string {alphabet} are {alphabet[0:3]}")
# so we are saying print index 0,1,2 but not 3!
# turns out we have syntax sugar for this
# if we omit start index it defaults to 0
print(f"First 3 characters in the string {alphabet} are {alphabet[:3]}")
first_3 = alphabet[:3]
print(first_3)
# so now we can get first ten easily
first_ten = alphabet[:10]
print(first_ten)
# now let's get last 5 characters from the string
# we could use positive indexing for this
print(f"Last 5 characters in the string {alphabet} are {alphabet[21:26]}")
# more interestingly I could use any large index without error when slicing
print(f"Last 5 characters in the string {alphabet} are {alphabet[21:26000]}")
# of course for longer strings this would generate different results
# but for the alphabet with length 26 it is the same as above

# even better would be to use negative indexing for this
# so I could say give me last 5 characters from the string
last_5 = alphabet[-5:] # this means give me all characters from -5 to the end of the string
print(f"Last 5 characters in the string {alphabet} are {last_5}")
# we can mix and match positive and negative indexing
# so I could say give me characters from 5 to -5
# this means give me characters from index 5 to index -5 (not included)
print(f"Characters from 5 to -5 in the string {alphabet} are {alphabet[5:-5]}")

# we have not mentioned step yet
# step is used to skip characters in the string
# let's get every second character from the string
# this is done by adding :step to the slice
print(f"Every second character in the string {alphabet} are {alphabet[::2]}")
# how about starting with b - that is 2nd character in the string
# and let's skip every 3rd character
# this is done by adding :step to the slice
print(f"Every 3rd character in the string {alphabet[1::3]} starting with b")

# note that we can use any variables for ALL 3 steps
start = 5
end = 20
step = 4
print(f"""Characters from {start} to {end} with step {step} in the string {alphabet} are:
        {alphabet[start:end:step]}""")

# now let's see a neat trick to reverse the string
# we can use slicing to reverse the string by using -1 as step
# this means give me all characters from start to end but in reverse order
reversed_alphabet = alphabet[::-1]
print(f"Reversed alphabet is {reversed_alphabet}")

# how about existance check - finding whether a character is in the string
# this is done using the in keyword

print(f"Is letter x in the string {alphabet}?")
print("x" in alphabet) 
needle = "op"
print(f"Is needle {needle} in the string {alphabet}?")
print(needle in alphabet)
bad_needle = "burp"
print(f"Is needle {bad_needle} in the string {alphabet}?")
print(bad_needle in alphabet)