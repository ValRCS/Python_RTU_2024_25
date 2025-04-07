# Eglīte
while True:
    try:
        pine_height = int(input("Ievadiet eglītes augstumu: "))
        # now we know that pine_height is integer but is it positive?
        if pine_height > 0:
            break
        # could use else: but not needed
        print("Skaitlim jābut pozitīvam!")
    except ValueError:
        print("Lūdzu ievadiet veselu pozitīvu nenulles skaitli")
 
for i in range(1, pine_height + 1):
    print(" " * (pine_height - i) + "*" * (2 * i - 1))