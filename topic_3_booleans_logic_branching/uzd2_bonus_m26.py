# 2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
# 
# Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
# 
# Izvadiet bonusu.
# 
# Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
 
parbaudes_laiks = 2
bonuss = 0.15
 
alga = input("Kāds ir Tavs atalgojums eiro naudiņās?  >>  ")

try:
    alga = int(float(alga)) # any error here will JUMP to except
    print("Veiksmīgi pārveidoju algu tīros eirikos")
except ValueError as e: # good practice is to catch specific Errors
    print(f"Kļūda nav skaitlis! Error: {e}")
    print(f"Nekā nebija, mums vajag veselus skaitļus Eiro")
    # here we just have to exit else we  have error
    print("Nāksies programmu pagaidām beigt, laižiet vien vēlreiz")
    # alternative would be to make alga here some int value 0 or 9000 or something..
    exit() # stops Program 
    
    
gadi = input("Cik gadus Tu jau esi pie šīs virpas?  >>  ")
gadi = int(gadi)
 
 
if gadi > parbaudes_laiks:
    plusini = gadi - parbaudes_laiks
    # Bonuss 15% no algas par katru gadu
    bonus = alga * bonuss * plusini
    print(f"Jauki! Šogad Zs atalgojumā kā bonusu Tev izmaksāsim papildus {bonus:.2f} eiro!")