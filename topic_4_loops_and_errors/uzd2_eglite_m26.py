# Uzdevums 2

while True:
    try:
        h = int(input("Ievadiet eglītes augstumu: "))
        # here we KNOW we have h as integer!
        if h > 0:
            break # means we got the right type of input
        # could use else: here but not needed
        print("Ievadam jābūt virs 0!")
    except ValueError:
        print("Lūdzu ievadiet veselu skaitli!")

# here we have h that meets our expectations
for i in range(1, h + 1):
    space = " " * (h - i) #definejam atsarpi  katrai rindai (height) atnemot izdruaks/iteraciju skaitu i  - 3 rindas - i (1) = 2 atsarpes
    star = "*" * (2 * i - 1) #definejam simbolu te tikai vajag vairâk zvaigznes, katra iterâcija tiekot pie nepâra skaitla
    print(space + star) #izdruka
