# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
while True:
    try:
        first_number = int(input("Ievadi sākuma skaitli: "))
        last_number = int(input("Ievadi beigu skaitli: "))
        # here i KNOW i have two good integers
        # so i can break out of the loop
        break
    except ValueError:
        print("Lūdzu ievadiet veselus skaitļus!") 
    # we go back to the start of the loop

# here we have two good integers
# and we can proceed to the next step

# tukšs saraksts
cubes = []

# let's use step 1 as default step
step = 1
if first_number > last_number:
    # if first number is greater than last number, we will use step -1
    step = -1
 
# cikls ar intervālu
for num in range(first_number, last_number + step, step):
    cube = num ** 3
    print(f"{num} kubā: {cube}")
    cubes.append(cube)
 
# Izvade visiem kubiem
print(f"Visi kubi: {cubes}")