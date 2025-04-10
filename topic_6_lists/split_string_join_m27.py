# it can be helpful to split a string into a list of words, and then join them back together
# for this Python offers string split() and join() methods
# split() method splits a string into a list where each word is a list item
# the split() method takes a separator as an argument, which specifies where to split the string
# default is any whitespace (space, newline etc.)
# join() method takes all items in an iterable and joins them into one string

sentence = "A quick brown fox jumps over the lazy dog"
print("Original sentence:", sentence)
# I can split the sentence into words using the split() method
words = sentence.split() # so deconstructuring the sentence into a list of words
print("List of words in the sentence:", words)
# now I can mutate this list of words
needle = "fox"
if needle in words:
    index = words.index(needle)
    print(f"Index of the word {needle}:", index)
    words[index] = "cat"
print("List of words after mutation:", words)

# now I can join them back together into a string using the join() method
# I can use the join() method to join the words back together into a sentence
# so constructuring the list of words into a sentence
# I can use any separator, but in this case I will use a space
joined_sentence = " ".join(words) # words must be list of strings
print("Joined sentence:", joined_sentence)

# in this example of course I could have used replace method instead of split and join
# but this is just to show how split and join work
# split and join will be useful for more complex string manipulations

# let's use cat emoji as separator for join
cat_separator = "🐱" # could be many chars
joined_sentence = cat_separator.join(words) # words must be list of strings
print("Joined sentence with cat separator:", joined_sentence)

# as mentioned we can use something else to split by
# let's say I have some , text
comma_text = "155, 1154  ,621  ,5,1,5,6"
print("Original comma separated text:", comma_text)
text_list = comma_text.split(",") # split by comma
print("List of numbers:", text_list)

# now I would need to convert them to integers
integer_list = []
for item in text_list:
    try:
        my_integer = int(item.strip()) # convert to int
    except ValueError:
        print(f"Could not convert {item} to int")
        continue
    integer_list.append(my_integer) # convert to int and append to list

print("List of integers:", integer_list)

# now I can sum them up etc
print("Total of the numbers:", sum(integer_list))

