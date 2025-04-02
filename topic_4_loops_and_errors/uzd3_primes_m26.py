# 3. Pirmskaitlis
# Atrodiet vai ievadītais veselais pozitīvais skaitlis ir pirmskaitlis.
# Pirmskaitlis ir skaitlis, kas dalās bez atlikuma tikai pats ar sevi un 1.
# Piezīme: šo uzdevumu var sākt risināt ļoti vienkārši un varat arī pēc tam optimizēt. 
# (kaut vai tas, ka mums nav jāpārbauda dalīšanās ar skaitļiem, kas lielāki par ievadītā skaitļa kvadrātsakni)
# import math # this is standard library built in Python
number=int(input("Ievadi skaitli: ")) # TODO add error checking

# maximum = int(math.sqrt(number))
maximum = int(number**0.5) 
print(maximum)
is_prime = True # we assume all numbers are prime until proven otherwise
for i in range(2,maximum+1):
    if number % i == 0:
        print(f"Oh oh {number} divides by {i} without reminder!")
        is_prime = False
        break
    
# flag is useful if we need to have some report or statement later 
if is_prime:
    print(f"Skaitlis {number} ir pirmskaitlis!")
else:
    print(f"Skaitlis {number} nav pirmskaitlis!")