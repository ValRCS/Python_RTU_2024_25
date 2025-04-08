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

# we could find exact index of the character in the string using find method
# this will return the index of the first occurrence of the character in the string
# if the character is not found it will return -1

needle_index = alphabet.find(needle)
print(f"Index of needle {needle} in the string {alphabet} is {needle_index}")
# so I could use that to get where I should start
print(f"Characters from {needle_index} to end of the string {alphabet} are {alphabet[needle_index:]}")
# how about starting where the needle ends
# then we simply need to add the length of the needle to the index
# so we can do this by using the find method and len function
print(f"Characters from {needle_index + len(needle)} to end of the string {alphabet} are {alphabet[needle_index + len(needle):]}")

# how about about the bad needle?
# this will return -1
bad_needle_index = alphabet.find(bad_needle)
if bad_needle_index == -1:
    print(f"Needle {bad_needle} not found in the string {alphabet}")
else:
    print(f"Aliens have landed")

# for strings we have an alternative to find method
# we can use index method
# this will return the index of the first occurrence of the character in the string
# if the character is not found it will raise an error
try:
    bad_needle_index = alphabet.index(bad_needle)
    # here we would know if we found the needle
    print("This will not show if the needle is not found")
except ValueError as e:
    print(f"Needle {bad_needle} not found in the string {alphabet}")
    print(f"ValueError: {e}")

# okay we can check for existence of the needle in the string using in keyword
# we can find the index of the needle in the string using find method

# let's loop through the string

# for that we use for loop using the in keyword
# this will loop through each character in the string
for char in alphabet:
    print(char, end=",") # this will print each character in the string
print() # this will print a new line

# we can use slice inside the for loop to get substrings from the string
# let's loop through only last 10 characters in the string
for char in alphabet[-10:]:
    print(char, end=",") # this will print each character in the string
print() # this will print a new line

# we can also use the range function to loop through the string
# this will loop through each index in the string
# this is not Pythonic but it is useful in some cases
for i in range(len(alphabet)):
    print(f"Index {i} letter -> {alphabet[i]}") # this will print each character in the string
print() # this will print a new line

# instead use the Pythonic approach 
# we use enumerate function to loop through the string
# this will loop through each index and character in the string
for i, char in enumerate(alphabet):
    print(f"Index {i} letter -> {char} == {alphabet[i]}") # this will print each character in the string
print() # this will print a new line

breakfast = "Auzu putra ar bieZpienu" 
print(breakfast)
# let's make it all lower case - soo quietly
print(breakfast.lower())
# now let's be loud and make it all upper case - YELLL
print(breakfast.upper())
# again note breakfast is unchanged
# this is because strings are immutable in Python
print(breakfast)
ALL_CAPS = breakfast.upper()
print(ALL_CAPS)

# we have more methods for strings
# let's capitalize the string
print("Capitalized:", breakfast.capitalize()) # this will capitalize the first character in the string
# let's title case the string
print("Title Case:", breakfast.title()) # this will capitalize the first character in each word in the string
# let's swap case the string
print("Swap Case:", breakfast.swapcase()) # this will swap case of each character in the string

# it is very typical to go through string and build a new string based on some advanced logic
# this is done using string concatenation
# this is done using the + operator
# we will use a blank buffer variable to build the string
buffer = "" # buffer is just a common name for a variable that is used to build a string
# let's loop through the string and build a new string based on some logic
for c in breakfast:
    # let's say we want to skip all spaces in the string
    if c == " ":
        continue
    elif c == "z":
        buffer += "AZA"
    else:
        buffer += c # this will build a new string based on the logic above

print(buffer) # this will print the new string

# we could use it to print all X's instead of letters
buffer = ""
for c in breakfast:
    # let's say we want to skip all spaces in the string
    if c == " ":
        buffer += " "
    else:
        buffer += "X" # this will build a new string based on the logic above

print(buffer) # this will print the new string

# instead of using buffer and looping many of the above operations
# can be done using built-in methods such as replace

# let's replace all u with y
new_breakfast = breakfast.replace("u", "y")
# if I wanted to overwrite the breakfast variable I could do it like this
# breakfast = breakfast.replace("u", "y")
print(new_breakfast) # this will print the new string

# let's see how we can use replace in conjuction with for loop
# we have some bad chars that we want to get rid of
# let's get rid of punctuation in our text
sentence = "Hello, Pythonistas! How are you? My Name is 'Bob'...or maybe not"
print(sentence) # this will print the original string
bad_chars = "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/~`"
clean_sentence = sentence # i want to keep the original sentence intact
for c in bad_chars:
    clean_sentence = clean_sentence.replace(c, "") # this will replace all bad chars with empty string
# let's see the clean sentence
print(clean_sentence) # this will print the new string
# note there is another way to do this with translation table

# let's clean up the city

dirty_city = "\t  \tRīga, Rīga, Rīga!  \n\t  \t"
print(dirty_city) # this will print the original string

# let's clean both sides with strip method
clean_city = dirty_city.strip() # this will remove all whitespace from both sides of the string
print(clean_city) # this will print the new string

# we could only clean one side of the string using lstrip and rstrip methods
# lstrip will remove all whitespace from the left side of the string
print(dirty_city.lstrip()) # this will remove all whitespace from the left side of the string
# similarly rstrip will remove all whitespace from the right side of the string
print(dirty_city.rstrip()) # this will remove all whitespace from the right side of the string