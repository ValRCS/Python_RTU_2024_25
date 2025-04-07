# 2. uzdevums - Karātavas
# secret_text = input("2. uzd. - Ievadi slepeno tekstu (player 1): ")

# buffer = ""
# for c in secret_text:
#     if c == " ":
#         buffer += " "
#     else:
#         buffer += "*"

# print(buffer)
# print("2. uzd. - Ievadi minējumu (player 2): ")
# guess = input()

# new_buffer = ""
# for c in secret_text:
#     if c == guess:
#         new_buffer += c # could use guess as well
#     elif c == " ":
#         new_buffer += " "
#     else:
#         new_buffer += "*"
# print(new_buffer)


secret_text = str(input('Ievadiet atminamo vārdu bez simboliem: \n'))
# we could normalize the text here with lower() or upper()
# secret_text = secret_text.lower()
print('Uzminamais vārds: ', end='')
guessed_letters = '' # since we do not know any other sequences we store our guesses in string
while True:
    print('\nUzminamais vārds: ', end='')
    current_guess = ""
    for c in secret_text:
        if c == ' ':
            print(' ', end='')  # atstarpene
            current_guess += ' '
        elif c in guessed_letters:
            print(c, end='')  # uzminets ?
            current_guess += c
        else:
            print('*', end='')  # paslepsi ?
            current_guess += '*'
    if current_guess == secret_text:
        print('\n🎉 Apsveicam! Tu atminēji vārdu!')
        break
    guess = input('\nIevadi burtu:\n ')[0].lower()
    guessed_letters += guess