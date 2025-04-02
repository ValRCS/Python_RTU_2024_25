#1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"
# print("Temperatūras pārbaudes uzdevums")
# temp = float(input("Kāda ir ķermeņa temperatūra? "))
 
# if temp < 35:
#     print("Vai nav vēsa sajūta?")
# elif 35 <= temp <= 37:
#     print("Jums viss ir kārtībā")
# else:
#     print("Jums iespējams ir drudzis")
# print("*"*50)

# 1. Uzdevums
kerm_temp = float(input("Ievadiet lūdzu Jūsu ķermena temperaturu: "))
if kerm_temp < 35:
    print("Vai Jums nav auksti?")
elif kerm_temp > 37:
    print("Jums iespejams ir drudzis.")
else:
    print("Ar Jums viss ir kartiba!")
 