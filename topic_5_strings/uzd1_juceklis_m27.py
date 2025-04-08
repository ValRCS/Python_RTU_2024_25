# Juceklis
# vards = input("Ievadi savu vārdu!")
# print((vards[::-1].capitalize()),", pamatīgs juceklis, vai ne", vards[0])

word = input("Ievadiet vārdu: ")
# let's check the suffix of the word for Latvian gender
if word.endswith("s"):
    print(f"Sveiks {word}!")
elif word.endswith("a"):
    print(f"Sveika {word}!")
else: # in Latvian we have "o" which can cover both genders, but let's keep it simple
    print(f"Summināti {word}!")

reversed_word = word[::-1]
word_capital = word[0].capitalize() # could have used upper or title as well because we only have one character
print(f"{word} -> {reversed_word.capitalize()}, pamatīgs juceklis, vai ne {word_capital}?")