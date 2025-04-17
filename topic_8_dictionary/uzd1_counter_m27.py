# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} # vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut
# def get_char_count(text):
#     result = {}
#     for char in text:
#         result[char] = result.get(char, 0) + 1
#         # so if there is no key char then we set it to 0 and add 1 to it
#     return result
#1.uzdevums
def get_char_count(text: str) -> dict[str, int]:
    char_count = {}
    for letter in text:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

print(get_char_count("hubba bubba"))

def get_digit_dict(num: int) -> dict[str, int]:
    # first set all 0 values for string keys 0-9
    digit_count = {str(d): 0 for d in range(10)}
    # above is a dictionary comprehension
    # it is equivalent to:
    # digit_count = {}
    # for d in range(10):
    #     digit_count[str(d)] = 0
    # but this is more compact and readable
    
    for digit in str(num):
        digit_count[digit] += 1
 
    return digit_count

big_num = 12332542354567890

print(get_digit_dict(big_num))

# in the case of counting digits we could have used a list...
# a rare case where list is similar to dictionary
# why? because our keys are 0-9 which nicely map to indexes of a list

def get_digit_list(num: int) -> list[int]:
    digit_count = [0] * 10
    
    for digit in str(num):
        digit_count[int(digit)] += 1
    
    return digit_count

print(get_digit_list(big_num))
# but this is not as readable as dictionary version

# we can also use Python's Counter to count things
# it gives you a dictionary like object that has some extra methods
# let's import it
from collections import Counter # typically we import at start of code
# but this is a special case where we want to show how to use it
my_counter = Counter("hubba bubba")
print(my_counter)
# what we get with Counter is a built in most_common method
print("Top 3 most common letters:")
print(my_counter.most_common(3)) # returns list of tuples (char, count)

# i can count other things  not only letters
# all i need to do is give Counter something iterable
foods = ["pizza", "burger", "pizza", "sushi", "burger", "burger"]
food_counter = Counter(foods)
print(food_counter)
# if I want plain dict it is easy to create from Counter
food_counter_dict = dict(food_counter)
print(food_counter_dict)
# but the most_common method is not available in plain dict

# so use Counter to count things!