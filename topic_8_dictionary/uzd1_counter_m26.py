def get_symbol_count(text):
    # to make it work on digits
    # we can simply convert the text to string
    text = str(text) # if text is already a string nothing happens
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else: # we do not have this letter in the dictionary yet
            char_count[char] = 1
    return char_count

# let's count abracadabra

abra_dict = get_symbol_count("abracadabra")
print(abra_dict)

# how about a number now
digit_dict = get_symbol_count(12335425616174567890)
print(digit_dict)
# how many times digit 1 ?
print(f"Digit 1 appears {digit_dict['1']} times")

# let's convert digit dictionary into keys being integers
# and values being counts as before

digit_dict_int = {}
for key, value in digit_dict.items():
    try:
        digit_dict_int[int(key)] = value
    except ValueError:
        # this means we have a non-integer key
        # let's just skip it
        print(f"Key {key} is not an integer, skipping")

# let's print the dictionary again
print(digit_dict_int)

# now we can convert this to a list of keys being indexes and values being counts

# let's create a list of zeros
digit_count_list = [0] * 10 # 10 digits
# now we can loop through the dictionary and set the counts
for key, value in digit_dict_int.items():
    digit_count_list[key] = value # key is the digit, value is the count

# let's print the list
print(digit_count_list)
# now we can loop through the list and print the counts

# instead of making our own counter we could have used built in Counter
from collections import Counter # typically this would be at the top of the file

# let's create a counter object
counter = Counter("abracadabra")
# let's print the counter object
print(counter) # counter is a dictionary with some extras
# i can get top 3 elements
print(counter.most_common(3)) # [('a', 5), ('b', 2), ('r', 2)]


# i can count also items in a list
foods = ["apple", "banana", "apple", "orange", "banana", "banana", "kiwi", "mango", "kiwi"]

# let's create a counter object
food_counter = Counter(foods)
# let's print the counter object
print(food_counter) # Counter({'banana': 3, 'apple': 2, 'kiwi': 2, 'orange': 1, 'mango': 1})
# i can get top 2 elements
print(food_counter.most_common(2)) # [('banana', 3), ('apple', 2)]