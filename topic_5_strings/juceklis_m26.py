# ========= 1 =================
name = input('Kāds ir Jūsu vārds?\n')
# let's check what letter is the word ends with
# if name[-1] == 's': #assumption being male genders in Latvian end with 's'
if name.endswith('s'): # ends with is useful for longer suffixes such as "is"
    # print('Sveiks, ', end='')
    greeting_start = 'Sveiks, '
else:
    # print('Sveika, ', end='')
    greeting_start = 'Sveika, '

# print(f'Sveiks, {name[0].upper()}{name[1:-1].lower()}, pamatīgs juceklis vai ne {name[0].upper()} ')
# print('Diemžēl ja ievadīji sieviešu vārdu, tad tavu vārdu rakstā tā, kā izrunā Kurzemniek')
name_reverse = name[::-1]
print(f'{greeting_start}{name_reverse[0].upper()}{name_reverse[1:].lower()}, pamatīgs juceklis vai ne {name[0].upper()}')
print(f'{greeting_start}{name[::-1].capitalize()}, pamatīgs juceklis vai ne {name[0].upper()}')