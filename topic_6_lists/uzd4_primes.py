# 4. Uzdevums
 
# TODO correct input prompt with try/except
# TODO add input validation
cik = int(input("Cik pirmos pirmskaitļus vēlaties atrast? "))
 
# pirmskaitli = []
# skaitlis = 2
 
# while len(pirmskaitli) < cik:  # outer loop
#     for i in range(2, int(skaitlis ** 0.5) + 1):
#         if skaitlis % i == 0:
#             break
#     else: # this else is part of for loop
#         # it will run IF the for loop is NOT broken
#         pirmskaitli.append(skaitlis)

#     skaitlis += 1

prime_list = [2]
prime_number = 3   #mazākais pirmskaitlis ?

while len(prime_list) < cik:
    is_prime = True
    for i in range(2, int(prime_number ** 0.5) + 1):
        if prime_number % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(prime_number)
    prime_number += 2 # only check odd numbers   

print(f"Pirmie {cik} pirmskaitļi:", prime_list)

# print(prime_list)