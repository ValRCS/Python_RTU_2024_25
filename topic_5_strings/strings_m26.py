print("Hello strings!")
# What are strings after all?
# Strings are sequences of characters
# Technically, strings are sequences of Unicode characters
# Python does not have single-character type
# Single characters are strings of length 1

# Strings are immutable

# let's start with some healthy food
food = "salmon"
# In Python there is no difference between single and double quotes
# They are interchangeable
drink = 'green tea'
# let's print the food and drink variables
print(food)
print(drink)

# we can use one quote inside another
# for example, we can use single quotes inside double quotes
# or double quotes inside single quotes
# let's see some examples
print("I love 'green tea'")
print('I love "green tea"')

# so what do we do if we want to use the same quote inside the string?
# we can use the backslash to escape the quote
# let's see some examples
print('I love \'green tea\'') # note how the backslash is used to escape the single quote
print("I love \"green tea\"") # note how the backslash is used to escape the double quote
# there are other escaped characters in Python
# for example, we can use \n to create a new line
# there is \t also \t to create a tab
# there is \rf to create a carriage return
# there is \b to create a backspace - RARELY USED
# there is \f to create a form feed - RARELY USED
# of course there is \\ to create a backslash
# let's see an example in one string
print("I \tlove 'green tea'\nI love \"green tea\"")

# if you do not want ANY escaping, you can use raw strings
# raw strings are created by adding an r before the string
# these can be useful if you are using regular expressions
# let's see some example
print(r"I \tlove 'green tea'\nI love \"green tea\"")

# for multi-line strings, we can use triple quotes
# triple quotes can be either single ''' or double quotes """
# I can put escaped characters in triple quotes inside triple quotes
some_long_string = """This is a long string
that \tspans multiple lines
and is very useful for long texts.
I can use 'single quotes' and "double quotes" inside it
without any escaping.
The End."""
print(some_long_string)

# we already know about f-strings
# we can use f-strings inside triple quotes
# let's see an example
recipe = """This is a recipe for {food} and {drink}
It is very healthy and delicious.
I love it.
Start by cooking the {food} in a pan.
Then drink the {drink} while you wait.
Finally, enjoy your meal!"""

print(recipe)

# now let's start talking about indexing
# to access a character in a string, we can use indexing
# indexing starts at 0 !
name = "Valdis"
print(name[0]) # prints V
# second character is at index 1
print(name[1]) # prints a
# how about the last character?
print(name[5]) # prints s - because it is 6th character

# how could we make this general?
# let's get length of the string
name_len = len(name)
print(name_len) # prints 6

# so we could do this to get the last character
print(name[name_len - 1]) # prints s - because it is 6th character
# ABOVE is not Pythonic way of doing this!
# Instead Python has a special index -1
# -1 means last character of the string
print(name[-1]) # prints s - because it is 6th character
alphabet = "abcdefghijklmnopqrstuvwxyz"
# let's print the first character of the alphabet
print(alphabet[0]) # prints a - because it is 1st character
print(alphabet[-1]) # prints z - because it is 26th character
# of course I could have used 25 instead of -1
print(alphabet[25]) # prints z - beca   se it is 26th character

# how about trying to exceed the length of the string?
try:
    print(name[6]) # IndexError: string index out of range because it is 7th character
except IndexError as e:
    print("IndexError: ", e)

# Slicing
# we might want to get more than one character from the string
# we can do this using slicing
# the next best thing since sliced bread!

# In Python we use :[start:end] to slice a string
# start is inclusive and end is exclusive
# let's get the first 3 characters of the string
print(name[0:3]) # prints Val - because it is 1st to 3rd character
# turns out 0 is not needed
print(name[:3]) # prints Val - because it is 1st to 3rd character

# we can use negative indexes in the slice as well
# let's get the last 3 characters of the string
print(name[3:]) # prints dis - because it is 4th to last character
print(name[-3:]) # prints dis - because it is 4th to last character#
# note if we did
print(name[-3:-1]) # prints di - because it is 4th to end excluding last character

substance = "glaciālais konglumerāts"
# let's get last 12 characters of the string
print(substance[-12:]) # prints konglumerāts - because it is 12th to last character

print(alphabet)
# turns out slices have a step as well
# we can use [start:end:step] to slice a string
# let's get every second character of alphabet
print(alphabet[::2]) # prints acegikmoqsuwy - because it is every second character
# how about we start on 2nd letter and then print every second character

print(alphabet[1::2]) # prints bdfhjlnprtvxz - because it is every second character starting from 2nd letter

# how start at 3rd letter go until 20th letter and take every 4th character?
print(alphabet[2:20:4]) # prints cgkos - because it is every 4th character starting from 3rd letter until 20th letter
print(alphabet[2:19:4]) # prints cgkos - because it is every 4th character starting from 3rd letter until 20th letter
print(alphabet[2:18:4]) # prints cgko - 
print(alphabet[18]) # again the stop is exclusive - not included in output

# we can use variables inside our slices
start = 2
end = 20
step = 4
print(alphabet[start:end:step]) # prints cgkos - because it is every 4th character starting from 3rd letter until 20th letter

# we can also use negative step to reverse the string
# let's reverse the string
reverse_alphabet = alphabet[::-1] # prints zyxwvutsrqponmlkjihgfedcba - because it is reversed string
print(reverse_alphabet)
# of course I did not have to save it
print(alphabet[::-1]) # prints zyxwvutsrqponmlkjihgfedcba - because it is reversed string
# we could use other negative steps but those are rarely used

# if I want my slices saved I need to assign them to a variable
first_five = alphabet[:5] 
print(first_five) # prints abcde - because it is first 5 characters

# Existance Checking
# now let's check if something exists in our alphabet
# we can use in keyword to check if something exists in our string
print("Is letter b in alphabet?", "b" in alphabet) # prints True - because b is in alphabet
# we can check longer substrings as well
print("is bcd in alphabet?", "bcd" in alphabet) # prints True - because bcd is in alphabet
print("is Abba in alphabet?", "Abba" in alphabet) # prints False - because Abba is not in alphabet
needle = "Abba"
print("is Abba in alphabet?", needle in alphabet) # prints False - because Abba is not in alphabet
# this is exact match - case sensitive!

# how about looping?
# let's go over my name again
for c in name: # c is arbitrary name for the character in the string, could be any variable name
    print(c) # prints each character in the name on a new line

# how about getting index of each character?
# we could use approach from other languages
for i in range(len(name)): # i is index of the character in the string
    print(f"Index {i} corresponds to {name[i]}") # prints each character in the name on a new line
# Avoid the above approach in Python!

# more Python would be to use enumerate
# enumerate gives us index and value at the same time
for i, c in enumerate(name): # i is index of the character in the string
    print(f"Index {i} corresponds to {c} == {name[i]}") # prints each character in the name on a new line

# let's use a loop to print a slice of my name by increasing character count
for i in range(1, len(name) + 1): # i is index of the character in the string
    print(name[:i]) # prints each character in the name on a new line
    # note how I use i inside the slice notation

food = "kartupelis" 
needle = "art"
# let's check if needle is in food
if needle in food:
    print(f"{needle} is in {food}")
else:
    print(f"{needle} is NOT in {food}")

bad_needle = "pele"
# let's check if needle is in food
if bad_needle in food:
    print(f"{bad_needle} is in {food}")
else:
    print(f"{bad_needle} is NOT in {food}")

# we can also find index of our substring in the string
# we can use index or find methods for search
art_index = food.index("art")
print(art_index) # prints 1 - because it is 2nd character

#  how about our bad_needle?
# if we know that that there is a possibily of not finding the substring we put our index in try/except block
try:
    bad_index = food.index(bad_needle)
    print(bad_index) # will not get to this part...
except ValueError as e:
    print(f"{bad_needle} is NOT in {food}")
    print("ValueError: ", e)

# if you prefer you can use another method - find
# the difference is that find returns -1 if not found
# let's see an example
good_index = food.find(needle)
print(good_index) # prints 1 - because it is 2nd character
bad_index = food.find(bad_needle)
print(bad_index) # prints -1 - because it is not found
# now you could check with if else to see if it is -1 or not

breakfast = "aUzu putra ar lāceņu ievārījumu"
print(breakfast)
# let's capitalize this
print(breakfast.capitalize()) # prints Auzu putra ar lāceņu ievārījumu - capitalizes first letter of the string
# note that this does not change breakfast
# if we want to save this we use same(overwritting) or new variable
cap_breakfast = breakfast.capitalize()
print(cap_breakfast) # prints Auzu putra ar lāceņu ievārījumu - capitalizes first letter of the string
# let's look at some more methods
# we have title
print(breakfast.title()) # prints Auzu Putra Ar Lāceņu Ievārījumu - capitalizes first letter of each word
# there is also swapcase
print(breakfast.swapcase()) # prints AuZU PUTRA AR LĀCEŅU IEVĀRĪJUMU - capitalizes first letter of each word
# let's yell - ALL CAPS
print(breakfast.upper()) # prints AUZU PUTRA AR LĀCEŅU IEVĀRĪJUMU - capitalizes first letter of each word
# and we have lower too - quiet
print(breakfast.lower()) # prints auzu putra ar lāceņu ievārījumu - capitalizes first letter of each word

# how about some replace, let's replace u with y
print(breakfast.replace("u", "y")) 
# again if we need this new food we need to save it
new_food = breakfast.replace("u", "y")
print(new_food) # prints Azyz putra ar lāceņu ievārījumu - capitalizes first letter of each word

# we can chain multiple commands
super_food = breakfast.replace("u", "y").replace("ā", "a").replace("ē", "e").upper()
print(super_food) 

text_with_punctuation = "Sveika pasaule! Drīz vakariņas?...."

# if we want to remove multiple characters we can use the following recipe
bad_chars = ".!?;:,-" # could be letters or anything
clean_text = text_with_punctuation # start with the original text
for bad_char in bad_chars:
    print("removing", bad_char)
    clean_text = clean_text.replace(bad_char, "") # replace the bad character with empty string
    # print(clean_text) # print the cleaned text
print("Cleaned", clean_text)
