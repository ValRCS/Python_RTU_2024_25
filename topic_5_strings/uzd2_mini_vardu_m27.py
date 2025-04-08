# 2. Uzdevums - Uzrakstīt programmu teksta simboola atpazīšanai
text_input = input("Pirmais spēlētāj, ievadiet tekstu (bez cipariem): ")
hidden_word = ""
for c in text_input:
    if c == " ":
        hidden_word += " " # I could have used c as well
    else:
        hidden_word += "*"
    # we would need continue if we had more conditions to check here
print(f"Paslēpts ievadītais vārds: {hidden_word}")

# second enters guess
print("Otrais spēlētāj, uzmini pirmā spēlētāja vārdu!")
guess = input("Ievadiet savu minējumu kā burtu: ")

buffer = ""
for c in text_input:
    if c == " ":
        buffer += " "
    elif c == guess:
        buffer += c
    else:
        buffer += "*"
print(f"Daļēji atpazīts vārds: {buffer}")

# big idea would be to store guesses in another variable
# we do knot know about lists
# so we can use another string for this