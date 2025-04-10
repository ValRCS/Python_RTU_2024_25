# # Saglabā lietotāja ievadi
# user_text = input("Lūdzu, ievadi tekstu: ")
 
# # Izdrukā ievadu bez izmaiņām
# print("Oriģinālais teksts:", user_text)
 
# # veidojam mainīgos, lai var mainīt vārdus
# var_1 = "nav"
# var_2 = "slikts"
 
# # meklē mainīgos tekstā
# index_1 = user_text.find(var_1)
# index_2 = user_text.find(var_2)
 
# # pārbauda, vai vārdi "nav" un "slikts" eksistē un "nav" ir pirms "slikts"
# if index_1 != -1 and index_2 != -1 and index_1 < index_2:
#     # sadala teikumu trīs daļās
#     start = user_text[:index_1]                       # vārdi pirms "nav"
#     middle = user_text[index_1 + len(var_1):index_2]  # vārdi starp "nav" un "slikts"
#     end = user_text[index_2 + len(var_2):]            # vārdi pēc "slikts"
 
#     # jaunie mainīgie, ar ko aizstāt meklējamos vārdus
#     var_3 = "ir"
#     var_4 = "labs"
 
#     # apvieno teikumu, aizvietojot "nav ... slikts" ar "ir ... labs"
#     # new_text = start + var_3 + middle + var_4 + end
#     new_text = start + var_3 + " " + var_4 + end # we do not need the middle
#     print("Pārveidotais teksts:", new_text)
# else: # default when the words are not found or in the wrong order
#     print("Pārveidotais teksts:", user_text)

user_input = input("Ievadiet tekstu: ")
print("Jūsu teksts: ", user_input)
 
if "nav" in user_input and "slikts" in user_input:
    nav = user_input.find("nav")
    slikts = user_input.find("slikts")
 
    if nav < slikts:
        slikts_beigas = slikts + len("slikts")
        aizvietosana = user_input[:nav] + "ir labs" + user_input[slikts_beigas:]
        print("Tā būs pareizāk: ", aizvietosana)
    else:
        print("Teksts kā es to redzu: ", user_input)
 
if "nav" in user_input and "slikta" in user_input:
    nav = user_input.find("nav")
    slikta = user_input.find("slikta")
 
    if nav < slikta:
        slikta_beigas = slikta + len("slikta")
        aizvietosana = user_input[:nav] + "ir laba" + user_input[slikta_beigas:]
        print("Tā būs pareizāk: ", aizvietosana)
    else:
        print("Teksts kā es to redzu: ", user_input)
 
if not "nav" in user_input or not "slikt" in user_input:
    print("Piekrītu tavam domu gājienam")
    print("Teksts kā es to redzu: ", user_input)