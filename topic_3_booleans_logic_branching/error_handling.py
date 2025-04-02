# Python offers another way of branching
# we can use so called
# try and except

try:
    input_text = input("Lūdzu ievadiet veselu skaitli:")
    print(f"Jūs ievadījāt {input_text} mēģināšu pārvēst par skaitli")
    number = int(input_text) # if we get error here we JUMP to except
    print(f"Veiksmīgi pārveidojām uz skaitli {number}")
    # here we would skip except since we got no errors
except ValueError as e:
    print("Nesanāca Jūsu ievadu pārvērst par skaitli")
    print(f"Kļūdas paziņojums {e}")
    print("Izejam no programmas jo nav nekas cits ko darīt šodien")
    exit()

print("Sāksim rēķināt")
print(number + 1_000_000)
# te parastā programma