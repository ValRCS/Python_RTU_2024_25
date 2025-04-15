# 3. Uzdevums - Apgrieztie vārdi
text_input = input("Ievadiet lūdzu tekstu: ")
words = text_input.split() # sadalam tekstu vārdos
# pēc noklusējum split() sadala pa jebkura daudzuma tukšumiem
# reversed_words = []
# for word in words:
#     reversed_words.append(word[::-1])
# above could have been done in one line with list comprehension:
reversed_words = [word[::-1] for word in words]

joined_sentence = " ".join(reversed_words).capitalize() # pievienojam vārdus atpakaļ tekstā, katru vārdu apgriežot
print(joined_sentence)