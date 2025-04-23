# def is_pangram(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
#     mytext = mytext.lower().replace(" ", "")  # noņemam atstarpes un pārvēršam uz maziem burtiem
#     for burts in a:
#         if burts not in mytext:
#             return False
#     return True

def is_pangram(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    #neignorē atstarpes, pēc saņemtiem smiekliem par manu kodu no AI, tika veikti labojumi
    mytext = mytext.lower()  # pārvēršam uz maziem burtiem
    # mytext = ''.join(c.lower() for c in mytext if c.isalpha())
    # we do not need the above line, because we are using set() to remove duplicates and spaces
    # and we are using lower() to convert to lowercase
    # we are testing whether all letters in the alphabet are present in the text
    return set(a) <= set(mytext) # same as set(a).issubset(set(mytext))

# let's test the function
print(is_pangram("Aizsargāsim dabu!"))  # False
hipiji = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku"
print(is_pangram(hipiji)) # True
print(is_pangram("Žiglēns čūsku fēmīkis, vārdā Ķencis, bļāva tā: 'Ņurdošā āža jupuļzupa ēd ģihenes!'"))

english_alphabet = "abcdefghijklmnopqrstuvwxyz"
# assert there are 26 letters in the English alphabet
assert len(english_alphabet) == 26, "tas nav angļu alfabēts"
print("Varam turpināt")
# let's test the function with the English alphabet
print(is_pangram("The quick brown fox jumps over the lazy dog", english_alphabet)) # True
print(is_pangram("The quick brown bear jumps over the lazy dog", english_alphabet)) # False