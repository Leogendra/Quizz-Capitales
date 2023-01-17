from random import randint
import os


def formate(ligne):
    ligne = ligne.lower()
    accents = { 'a': ['à', 'ã', 'á', 'â'],
                'e': ['é', 'è', 'ê', 'ë'],
                'i': ['î', 'ï'],
                'u': ['ù', 'ü', 'û'],
                'o': ['ô', 'ö'], 
                '' : [' ', '-', '_', '\'', '(', ')', '"'] }
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            ligne = ligne.replace(accented_char, char)
    return ligne



def Capitales(mode, capitales, pays):
    numQuestion = randint(0,len(pays)-1)
    paysActuel = pays[numQuestion]
    capitaleActuelle = capitales[numQuestion]
    appelationPays = paysActuel
    paysNom = ""
    reponse = ""
    #print(f"[DEBUG] Pays : {paysActuel}, capitale : {capitaleActuelle}")

    # Recherche du pays et de la capitale
    resultat = paysActuel.split()
    if (len(resultat) > 1) :
        paysNom = resultat[0]
        paysArticle = resultat[1].replace("(", "").replace(")", "")
        if (paysArticle == "le"): appelationPays = "du " + paysNom
        elif (paysArticle == "les"): appelationPays = "des " + paysNom
        elif (paysArticle == "l'"): appelationPays = "de l'" + paysNom
        else: appelationPays = "de " + paysArticle + " " + paysNom
    else:
        paysNom = resultat[0]
  
    if (mode == 1):
        while (reponse == ""):
            reponse=input(f"Quelle est la capitale {appelationPays} ? ")
        bravo = "Bravo" if (formate(reponse) == formate(capitaleActuelle)) else "Dommage"
        print(f"{bravo} ! La réponse était : {capitaleActuelle}")

    if (mode == 2):
        while (reponse == ""):
            reponse=input(f"De quel pays {capitaleActuelle} est la capitale ? ")
        bravo = "Bravo" if (formate(reponse) == formate(paysNom)) else "Dommage"
        print(f"{bravo} ! La réponse était : {paysNom}")
    
    return bravo


def Departements(mode, departement, numeros, regions):
    numQuestion = randint(0,len(departement)-1)
    departementActuel = departement[numQuestion]
    numeroActuel = numeros[numQuestion]
    regionActuelle = regions[numQuestion]
    reponse = ""
    #print(f"[DEBUG] Département : {departementActuel}, numéro : {numeroActuel}, région : {regionActuelle}")

    if (mode == 3):
        while (reponse == ""):
            reponse = input(f"Quel est le numéro du département {departementActuel} ? ")
        bravo = "Bravo" if (formate(reponse) == formate(numeroActuel)) else "Dommage"
        print(f"{bravo} La réponse était : {numeroActuel}")

    if (mode == 4):
        while (reponse == ""):
            reponse = input(f"Quel est le nom du département {numeroActuel} ? ")
        bravo = "Bravo" if (formate(reponse) == formate(departementActuel)) else "Dommage"
        print(f"{bravo} ! La réponse était : {departementActuel}")

    if (mode == 5):
        while (reponse == ""):
            reponse = input(f"De quelle région est {departementActuel} ({numeroActuel}) ? ")
        bravo = "Bravo" if (formate(reponse) == formate(regionActuelle)) else "Dommage"
        print(f"{bravo} La réponse était : {regionActuelle}")
    
    return bravo


modes = [1, 2, 3, 4, 5, 6]
while(True):
    os.system("cls")
    points=0
    mode = 0

    #selection du mode de jeu
    print("Modes de jeu (0 pour quitter) :")
    print("1 : deviner les capitales")
    print("2 : deviner les pays")
    print("3 : deviner les numéros des départements")
    print("4 : deviner les noms des département")
    print("5 : deviner les régions des départements\n6 : aléatoire")
    while not(mode in modes):
        try:
            mode=int(input("\nChoisissez votre mode de jeu : "))
        except ValueError:
            print("Mode de jeu incorrect")
        
        if (mode == 0):
            exit()

    random = False
    if mode == 6:
        random = True
    

    #Nombres des questions
    nbrQuestions = 0
    while (nbrQuestions < 1):
        try:
            nbrQuestions=int(input("Nombre de questions : "))
        except ValueError:
            print("Nombre de questions incorrect")


    #Récupération des données
    if mode in [1, 2, 6]:
        pays=[]
        capitales=[]
        with open("capitales.txt", "r", encoding='utf8') as fd:
            for ligne in fd:
                mots=ligne.split(",")
                pays.append(mots[0])
                capitales.append(mots[1].strip())

    if mode in [3, 4, 5, 6]:
        numeros = []
        departements = []
        regions = []
        with open("departements.txt", "r", encoding='utf8') as fd:
            for ligne in fd:
                ligne=ligne.split(",")
                numeros.append(ligne[0].strip())
                departements.append(ligne[1].strip())
                regions.append(ligne[3].strip())



    #Quizz
    numQuestion = 1
    while (numQuestion <= nbrQuestions):
        print(f"\nQuestion {numQuestion}")

        if random:
            mode = randint(1, 5)

        if mode in [1, 2]:
            reponse = Capitales(mode, capitales, pays)
        if mode in [3, 4, 5]:
            reponse = Departements(mode, departements, numeros, regions)

        if (reponse == "Bravo"):
            points += 1

        numQuestion += 1


    #Affichage du score
    print(f"\n\nScore : {points}/{nbrQuestions}")
    input("Appuyez sur une touche pour continuer")