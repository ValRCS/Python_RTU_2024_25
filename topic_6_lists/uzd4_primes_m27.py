# 4. Uzdevums - Pirmskaitļi
while True:
    try:
        prime_amount = int(input("Ievadi cik pirmskaitļus vēlies redzēt: "))
        break
    except ValueError:
        print("Kļūda, netika ievadīts vesels skaitlis.")

prime_list = [2] # sākam ar 2, jo tas ir pirmais pirmskaitlis
number = 3 # sākam ar 3, jo 2 jau ir sarakstā
prime_count = 1 # viens jau mums ir sarakstā, tāpēc sākam ar 1
while prime_count < prime_amount: # outer loop
    is_prime = True
    # we do not have to check until number-1
    # we only need to check until sqrt(number)
    # because if number is divisible by n, then it is also divisible by number/n
    for n in range(2, int(number**0.5)+1): # inner loop that checks if number is prime
        if number % n == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(number)
        prime_count += 1
    number += 2 # we only check odd numbers, because even numbers are not prime (except 2)
print(prime_list)