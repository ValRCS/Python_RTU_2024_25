# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk
 
print('Kubinātors')
while True:
    try:
        start = int(input('Ievadiet sākuma skaitli: '))
        end = int(input('Ievadiet beigu skaitli: '))
        # here both start and end are integers for sure
        break
    except ValueError:
        print('Lūdzu ievadiet veselus skaitļus!')

cube_list = []
step = 1 # default step is 1
if start > end:
    step = -1
for i in range(start, end + step, step):
    cube = i ** 3
    print(f'{i} kubā: {cube}')
    cube_list.append(cube)
print(f'Visi kubi: {cube_list}')