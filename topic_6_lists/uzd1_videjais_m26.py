print('Programma, kas lietotājam liek ievadīt skaitļus.')
print('Ja vēlaties iziet no programmas ievadiet "q"')
number_input = input("Ievadiet skaitli:")
number_history = []
while number_input != "q":
    try:
        number = float(number_input)
    except ValueError:
        print("Lūdzu ievadiet skaitli vai 'q' lai izietu no programmas")
        number_input = input("Ievadiet skaitli:")
        continue
    # here we know we have a number!
    number_history.append(number)
    # total_numbers += number
    average_number = sum(number_history) / len(number_history)
    # sum works on numeric lists, and len gives us the number of items in the list
    print(f'\nSkaitļu vidējais ir {average_number:.4f},līdz šim ievadītie skaitļi {number_history}')
    print(f'3 lielākie ievadītie skaitļi ir:\n {sorted(number_history, reverse=True)[:3]}')
    print(f'3 mazākie ievadītie skaitļi ir: \n{sorted(number_history)[:3]}')
    number_input = input("Ievadiet skaitli:")
 
print(f'Jūsu ievadīto skaitļu vidējā summa ir {average_number}')