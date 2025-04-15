#2. uzdevums
def is_palindrome(text: str) -> bool:
    """This function checks if the given text is a palindrome.
    The function takes one parameter:
    text ->> str"""
    # first normalize text
    # this means lowercase and remove spaces
    normalized_text = text.lower().replace(" ", "")
    # now for the result you do NOT need if statement as example:
    # if normalized_text == normalized_text[::-1]:
    #     return True
    # else:
    #     return False
    # above is anti-pattern because it is not necessary to use if statement here

    return normalized_text == normalized_text[::-1]
# bad style would be to use if statement here, because we don't need to check if the text is a palindrome, we just need to return the result of the comparison
# this is a one-liner function, so we don't need to use if statement