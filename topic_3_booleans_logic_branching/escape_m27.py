print('Laipni lūdzam spēlē "Izlaušanās no mājas"!')
print('Veicot scenārija izvēli raksti attiecīgā scenārija numuru "1" vai "2".\n')

print("Tu pamosties istabā ar divām durvīm un divām numurētām atslēgām. Caur pirmajām durvīm var dzirdēt cilvēku balsis, no otrajām durvīm nav dzirdams nekas.")
# Iegūst lietotāja izvēlētās atbildes numuru
jaut1 = int(input("Ko Tu dari? (1. Atver pirmās durvis) (2. Atver otrās durvis):"))
# Pārbauda vai lietotājs ir izvēlējies pareizo atbildi. Kļūdainas ievades apstrāde pagaidām netiek veikta.
if jaut1 == 2:
    # Pareizas atbildes gadījumā tiek dota informācija par nākamo situāciju.
    print("\nTu atver otrās durvis, aiz kurām ir kāpnes uz ēkas jumtu. Uz jumta redzama novilkta trose no jumta līdz teritorijas žogam, kā arī balkons stāvu zemāk, no kura plīvo aizkari.")
else:
    # Nepareizas atbildes gadījumā lietotājam tiek paziņots, ka atbilde nav pareiza un tiek apstādināta programma.
    print("\nTu atver pirmās durvis un apsargi tevi noķer. :(")
    exit()
# Pēc šādas loģikas strādā katra nākamā spēles situācija.

jaut2 = int(input("Ko Tu dari? (1. Nolec uz stāvu zemāk esošo balkonu) (2. Rāpies pa trosi līdz žogam): "))
if jaut2 == 1:
    print("\nTev izdodas nolekt uz balkonu zemāk un ieiet atpakaļ mājā. Tu pieej pie atvērtajām durvīm istabā un tālāk redzi gaiteni. Gaitenim pa vidu ir centrālās kāpnes, gaiteņa galā ir evakuācijas izeja.")
else:
    print("\nTu rapies pa trosi līdz žogam un galā tevi sagaida apsargs, kurš tevi noķer. :(")
    exit()

jaut3 = int(input("Ko Tu dari? (1. Ej lejā pa centrālajām kāpnēm) (2. Skrien uz evakuācijas izeju): "))
if jaut3 == 2:
    print("\nTu izej no ēkas pa evakuācijas izeju. Priekšā ir taciņa, kura ved ārpus ēkas teritorijas. Blakus taciņai guļ suns.")
else:
    print("\nNoejot lejā pa centrālajām kāpnēm Tev priekšā stāv apsargs, kurš tevi noķer. :(")
    exit()

jaut4 = int(input("Ko Tu dari? (1. Skrien garām sunim, ārā no ēkas teritorijas) (2. Pamet sunim kaulu, kuru Tu atrodi blakus evakuācijas izejai.): "))
if jaut4 == 2:
    print("\nTu pamet sunim kaulu, un tas sāk to grauzt. Pa to laiku tu skrien pa taciņu ārā no ēkas teritorijas. Apsveicu, esi izbēdzis no mājas!")
else:
    print("\nSkrienot garām sunim tas pamostās un sāk riet. To sadzird apsargi un tevi noķer. :(")
    exit()