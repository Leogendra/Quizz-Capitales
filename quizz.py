from random import randint
import re

def quizz(mode):
    global capitales, pays
    if mode==3:
        mode=randint(1,2)
  
    print(f"\nQuestion {nbr-nbrq}")
    num_question = randint(0,len(pays)-1)
    pays_actuel=pays[num_question]
    capitale_actuelle=capitales[num_question]
    pays_complet=""
    reponse=""

    resultat=re.search("(.+) \((.+)\)",pays_actuel)
    if resultat :
        if resultat.group(2)=="le":
            pays_complet="du "+resultat.group(1)
        elif resultat.group(2)=="le":
            pays_complet="de "+resultat.group(2)+resultat.group(1)
        else:
            pays_complet="de "+resultat.group(2)+" "+resultat.group(1)
  
    if mode==1:
        print("Quelle est la capitale",pays_complet," ?")
        while reponse=="":
            try:
                reponse=input("")
            except:
                reponse=""
        print("La réponse était : ",capitale_actuelle)
        return reponse==capitale_actuelle
    else:
        print("De quel pays",capitale_actuelle,"est la capitale ?")
        while reponse=="":
            try:
                reponse=input("")
            except:
                reponse=""

        print("La réponse était : ",resultat.group(1))
        return resultat.group(1)==reponse


while(1):
    #selection du mode de jeu
    modes = [1, 2, 3]
    print("Modes de jeu :\n1 : deviner les capitales \n2 : deviner les pays, \n3 : aléatoire")
    mode = 0
    while not(mode in modes):
        try:
            mode=int(input("Mode de jeu : "))
            if (mode == 0):
                exit()
        except:
            print("Mode de jeu incorrect")

    #Initialisation des listes
    pays=[]
    capitales=[]
    with open("capitales.txt", "r") as fd:
        for ligne in fd:
            mots=ligne.split(",")
            pays.append(mots[0])
            capitales.append(mots[1].strip())

            

    #Nombres des questions
    nbr=int(input("Nombre de questions (0 pour quitter) : "))
    nbrq=nbr

    #Quizz pour le nombre de question
    pts=0
    while nbrq>0:
        nbrq-=1
        if quizz(mode):
            #si bonne réponse : +1pts
            pts+=1


    #Affichage du score
    print("\n\nScore : ",pts,"/",nbr)