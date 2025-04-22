# 3. Uzdevums - Vai ir pangramma?
 
def is_pangram(my_text:str, a = "abcdefghijklmnopqrstuvwxyz"):
    my_text_set = set(my_text.lower())
    my_text_set.remove(" ")
 
    alphabet = set(a)
    # we now test whether our set of letters in the text is a superset of the alphabet
    # this means that all letters in the alphabet are present in the text
    return my_text_set >= alphabet # same as my_text_set.issuperset(alphabet)

 
print(is_pangram("abcd foo"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The five boxing wizards jump quickly"))

# let's try with the Latvian alphabet
latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
# assert there are 33 letters in the Latvian alphabet
# assert throws an AssertionError if the condition is not met
# assert does nothing if the condition is True
assert len(latvian_alphabet) == 33, "tas nav latviešu alfabēts"
krekli = "Četri balti krekli ar melnu piedurkni zilā krūšturī"
print(is_pangram(krekli, latvian_alphabet)) # False
# let's find out which letters are missing by taking a set difference
missing_letters = set(latvian_alphabet) - set(krekli.lower())  
print(f"Krekli trūkst šādi burti: {missing_letters}") 


hipiji = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku"
print(is_pangram(hipiji, latvian_alphabet)) # True