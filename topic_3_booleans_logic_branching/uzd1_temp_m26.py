# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# 
#     Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
#     Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
#     Ja ir pāri 37, tad izvadiet "iespējams drudzis"
 
 
temp = float(input("Jūsu ķermeņa temp = "))
 
if temp < 35:
    print("Vai nav par aukstu ?")
elif temp <= 37:
    print("Ir OK")
else:
    print("Jums iespējams drudzis")