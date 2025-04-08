# 2. Uzdevums - Uzrakstīt programmu teksta simboola atpazīšanai
secret_word = input("Pirmais spēlētāj, ievadiet tekstu (bez cipariem): ")
# hidden_word = ""
# for c in text_input:
#     if c == " ":
#         hidden_word += " " # I could have used c as well
#     else:
#         hidden_word += "*"
#     # we would need continue if we had more conditions to check here
# print(f"Paslēpts ievadītais vārds: {hidden_word}")

# # second enters guess
# print("Otrais spēlētāj, uzmini pirmā spēlētāja vārdu!")
# guess = input("Ievadiet savu minējumu kā burtu: ")

# buffer = ""
# for c in text_input:
#     if c == " ":
#         buffer += " "
#     elif c == guess:
#         buffer += c
#     else:
#         buffer += "*"
# print(f"Daļēji atpazīts vārds: {buffer}")

# big idea would be to store guesses in another variable
# we do knot know about lists
# so we can use another string for this

# TODO add counter for wrong guesses
# TODO add MAX_GUESSES variable to limit the number of guesses

all_guesses = ""
while True:
    buffer = ""
    for c in secret_word:
        if c == " ":
            buffer += " "
        elif c in all_guesses:
            buffer += c
        else:
            buffer += "*"
    # let's check if we can finish the game
    if buffer == secret_word:
        print(f"Tu uzminēji vārdu: {buffer} 🎉")
        break

    print(f"Current guess: {buffer}")
    guess = input("Ievadiet savu minējumu kā burtu: ")[0] # we only need the first character
    # TODO add check if guess was already used
    print(f"Your guess is: {guess}")
    all_guesses += guess # we add our guess to the list of guesses

# TODO for actual final project would be to add printing of images or ascii art
# TODO for final project it would be nice to read predefined words from a file or online source

# TODO we can rewrite this using list data structure when we learn it :)