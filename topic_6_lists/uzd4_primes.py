# 4. Uzdevums
 
# TODO correct input prompt with try/except
# TODO add input validation
cik = int(input("Cik pirmos pirmskaitļus vēlaties atrast? "))
 
pirmskaitli = []
skaitlis = 2
 
while len(pirmskaitli) < cik:  # outer loop
    for i in range(2, int(skaitlis ** 0.5) + 1):
        if skaitlis % i == 0:
            break
    else: # this else is part of for loop
        # it will run IF the for loop is NOT broken
        pirmskaitli.append(skaitlis)
        
    skaitlis += 1

print(pirmskaitli)