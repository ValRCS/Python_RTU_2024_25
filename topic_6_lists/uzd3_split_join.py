# 3. Uzdevums
 
 
teksts = input("Ievadiet tekstu = ")

matrica = teksts.split() # we split the text into words into a list
 
 
# word_list = []
# for word in matrica:
#     word_list.append(word[::-1])
# i can replace the above with list comprehension
word_list = [word[::-1] for word in matrica]
final = " ".join(word_list).capitalize()

print(final)