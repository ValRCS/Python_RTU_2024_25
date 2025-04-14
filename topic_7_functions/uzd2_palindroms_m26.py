#2. Palindroms
#uzrakstiet funkciju is_palindrome(text)
#kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
#PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
#is_palindrome("Alus ari ira      sula") -> True
 
def is_palindrome(text: str) -> bool:
    """Funkcija pārbauda, vai teksts ir palindroms.
    Ievade:
    text: teksts - str\n\n
    Izvade:
    True, ja teksts ir palindroms, pretējā gadījumā False - bool
    """
    # Noņem atstarpes un pārvērš tekstu par maziem burtiem
    modified_text = ''.join(text.split()).lower()
    # Salīdzina tekstu ar tā apgriezto versiju
    # note we do not need to check with if here
    # antipattern would be 
    # if modified_text == modified_text[::-1]:
    #     return True
    # else:
    #     return False
    # we can just return the result of the comparison
    return modified_text == modified_text[::-1]
 
print(is_palindrome("Alus ari ira      sula"))  # Izvade: True# not
print(is_palindrome("Karlis"))  # Izvade: False
print(is_palindrome("Karlis ir ri   \t\n Silrak"))  # Izvade: True