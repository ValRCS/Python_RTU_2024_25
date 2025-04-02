# Izveido spēli ar vairākiem soļiem un divām izvēlēm katrā no soļiem.

# Pirmais paziņojums.
print("Tu pamosties slēgtā telpā. Uz galda ir atslēga, un logs ir nedaudz pavērts.")
# Spēlētājam jāveic izvēle starp diviem scenārijiem, norādot ciparu 1 vai 2.
step_one = int(input("Ko tu izvēlies darīt? 1: Paņem atslēgu, 2: Kāp ārā pa logu. Uzraksti izvēles ciparu: "))

# Kas notiek, ja spēlētājs izvēlas 1?
if step_one == 1:
    print("Tu esi gudrinieks - kapā tālāk!")
# Kas notiek, ja spēlētājs izvēlas jebko citu?
else:
    print("Tu mēģināji izkāpt, bet tas ir par augstu. Tu nokriti. Kaput.")
    exit() # Izvēloties jebko citu, spēle tiek izbeigta.

# Otrais paziņojums.
print("Tu pieej aizslēgtajām durvīm. Atslēga, ko paņēmi, der slēdzenei. Tu dzirdi soļus ārpusē.")
# Spēlētājam jāveic izvēle starp diviem scenārijiem, norādot ciparu 1 vai 2.
step_two = int(input("Vai tu atver durvis vai pagaidi? 1: Atver durvis, 2: Pagaidi. Uzraksti izvēles ciparu: "))

# Kas notiek, ja spēlētājs izvēlas 1?
if step_two == 1:
    print("Pareizi, draudziņ, vari kratīties tālāk.")
# Kas notiek, ja spēlētājs izvēlas jebko citu?
else:
    print("Tu gaidīji pārāk ilgi, un kāds tevi ieslēdza. Būtu labāk pa logu lecis ārā.")
    exit() # Izvēloties jebko citu, spēle tiek izbeigta.
    
# Trešais paziņojums.
print("Tagad tu esi virtuvē. Ir durvis, kas ved ārā, bet signalizācija ir ieslēgta.")
# Spēlētājam jāveic izvēle starp diviem scenārijiem, norādot ciparu 1 vai 2.
step_three = int(input("Ko tu dari? 1: Atslēdz signalizāciju, 2: Skrien caur durvīm. Uzraksti izvēles ciparu: "))

# Kas notiek, ja spēlētājs izvēlas 1?
if step_three == 1:
    print("You are The One! Paņem cepumu.")
# Kas notiek, ja spēlētājs izvēlas jebko citu?
else:
    print("Tev tika dotas visas iespējamās norādes uz SIGNALIZĀCIJU. Kāda velna pēc tu tomēr nolēmi kaut kur skriet? Kaput.")
    exit() # Izvēloties jebko citu, spēle tiek izbeigta.