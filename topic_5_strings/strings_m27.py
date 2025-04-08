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