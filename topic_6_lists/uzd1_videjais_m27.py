# list_of_numbers = []
 
# while True:
#     user_input = input("Ievadiet skaitli vai 'q' lai aizvērt programmu: ")
    
#     if user_input.lower() == 'q':
#         break
 
#     try:
#         user_number = float(user_input)
#         list_of_numbers.append(user_number)
#         average = sum(list_of_numbers) / len(list_of_numbers)
#         print("Ievadīto skaitļu saraksts: ", list_of_numbers)
#         print("Vidējā izveidotā saraksta vērtība ir: ", average)
#     except ValueError:
#         print("Neizskatās pēc skaitļa!")
 
# print("Programma pārtraukta. Gaidīsim Jūs vēlāk!")

# Klases uzdevumi - Lists
 
# 1. Uzdevums - vidējā vērtība
print("Starting average value program")
number_list = []
while True:
    user_input = input("Ievadiet skaitļus, vai (q vai Q) lai izietu no programmas: ")
    if user_input.lower() == "q": # Ja lietotājs ievada "q", tad tiek apstādināta programma
        print("Programma apstādināta.")
        break
    try: # Tiek pārbaudīts vai lietotājs ievadīja skaitli
        number = float(user_input)
    except ValueError: # Ja nav ievadīts skaitlis, tad tas tiek paziņots un tiek vēlreiz jautāts ievadīt skaitli
        print("Kļūda, netika ievadīts skaitlis.")
        continue # go back to the start of loop
    # now we can start actually using the number
    number_list.append(number)
    average_val = sum(number_list) / len(number_list)
    print(f"Visu lidz šim ievadīto skaitļu vidējā vērtība: {average_val:.2f}")
    print(f"Visi ievadītie skaitļi: {number_list}")
    sorted_list = sorted(number_list)
    top3_numbers = sorted_list[-3:]
    bottom3_numbers = sorted_list[:3]
    print(f"Trīs lielākie skaitļi sarakstā: {top3_numbers}. Trīs mazākie skaitļi sarakstā: {bottom3_numbers}")