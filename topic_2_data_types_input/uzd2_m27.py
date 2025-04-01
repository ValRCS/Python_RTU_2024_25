#Uzdodied 3 jautājumus par telpas platumu, garumu, augstumu Uzrādiet cik liels būs telpas tilpums
width = float(input("Ievadiet telpas platumu (metros): "))
length = float(input("Ievadiet telpas garumu (metros): "))
height = float(input("Ievadiet telpas augstumu (metros): "))
volume = width * length * height
print(f"Telpas tilpums ir {volume:.2f} kubikmetri jeb m³.\n")
# we can add some padding (reserved space for our variable)
print(f"Telpas tilpums ir {volume:15.2f} kubikmetri jeb m³.\n")