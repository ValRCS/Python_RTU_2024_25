print('Laipni lūdzam spēlē "Izkļūšana no mājas!"')
# 1. scenārijs
# Maza slēgta istaba ar galdu ar atvilkni un 2 kastītēm uz galda. Kopā 3 atslēgas. Durvīm der atslēga no atvilktnes
no_exit_from_scenario = True
print("Slēgtā istabā ir galds ar atvilktni un uz galda ir divas kastītes.")
print("Pa atslēgai atrodas atvilknē un katrā kastītē.")
while no_exit_from_scenario:
    next = True
    while next:
        try:
            izvele = int(input(f"Tu vari paņemt atslēgu no pirmās kastītes - raksti 1, atslēgu no otrās kastītes - raksti 2 vai atslēgu no atvilknes - raksti 3 "))
            if izvele==1 or izvele==2 or izvele==3:
                next=False
                break # ja ievadīts 1 vai 2 vai 3
            else:
                next=True
                print("Kļūda! Lūdzu, izdariet izvēli: 1 , 2 vai 3!")
        except ValueError:
            print("Kļūda! Lūdzu, izdariet izvēli: 1 , 2 vai 3!")
    if izvele==3:
        print("Atslēga der. Dodamies tālāk!")
        no_exit_from_scenario=False
    else:
        print("Atslega neder. Jāņem citu!")
        no_exit_from_scenario=True
# ---
# 2. scenārijs
# trīs durvis = derēs vidējās 
no_exit_from_scenario = True
print("Tu nonāci istabā, kur pretējā sienā ir 3 durvis.")
while no_exit_from_scenario:
    next = True
    while next:
        try:
            izvele = int(input(f"Tu vari iet pa kreisajām - raksti 1, iet pa labajām - raksti 2 vai iet pa vidējām - raksti 3 "))
            if izvele==1 or izvele==2 or izvele==3:
                next=False
                break # ja ievadīts 1 vai 2 vai 3
            else:
                next=True
                print("Kļūda! Lūdzu, izdariet izvēli: 1 , 2 vai 3!")
        except ValueError:
            print("Kļūda! Lūdzu, izdariet izvēli: 1 , 2 vai 3!")
    if izvele==3:
        print("Īstās durvis. Dodamies tālāk!")
        no_exit_from_scenario=False
    elif izvele==1:
        print("Šīs ir pieliekamā durvis. Jāizvēlas citas!")
        no_exit_from_scenario=True
    else:
        print("Šīs ir drēbju skapja durvis. Jāizvēlas citas!")
        no_exit_from_scenario=True
# ---
# 3. scenārijs
# Virtuvē Jāieslēdz gaisma lai ieraudzītu izeju
no_exit_from_scenario = True
print("Tu nonāci virtuvē, kur it tumšs kā peklē.")
while no_exit_from_scenario:
    next = True
    while next:
        try:
            izvele = int(input(f"Tu staigā apkārt uzgrūžoties visādām lietām - raksti 1, ieslēgt gaismu - raksti 2"))
            if izvele==1 or izvele==2:
                next=False
                break # ja ievadīts 1 vai 2
            else:
                next=True
                print("Kļūda! Lūdzu, izdariet izvēli: 1 vai 2!")
        except ValueError:
            print("Kļūda! Lūdzu, izdariet izvēli: 1 vai 2!")
    if izvele==2:
        print("Gaismā var redzēt izejas durvis. Tu esi brīvs!")
        no_exit_from_scenario=False
    else:
        print("Tu uzgrūdies ledusskapim un viņš ir mazliet sarūgtināts. Jāizvēlas Kaut kas cits!")
        no_exit_from_scenario=True
print("Apsveicu!")
# ---

    