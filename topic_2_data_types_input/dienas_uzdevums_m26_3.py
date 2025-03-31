print("Programma, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc Fārenheita un Kelvina skalām")
SI = input("Kāda ir temperatūra pēc Celsija? ℃ ")
IMPERIAL = 32+float(SI)*1.8
SI_KELVIN = float(SI) + 273.15
print(f"Līdzīga temperatūra pēc Farenheita skalas būs {IMPERIAL:.2f} ℉.")
print(f"Attiecīgi temperatūra pēc Kelvina skalas būs {SI_KELVIN:.2f} grādi.")