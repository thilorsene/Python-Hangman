import random as random
def chargement():
# ouverture du fichier des mots
    fichier = open('c:/Users/thilo/Desktop/M1/S1/Algo et Complexité/Projet Hanglan/mot.txt', 'r')
    i=0
    liste_debutant = []
    liste_intermediaire = []
    liste_experimente = []
# Classification des mots dans les listes suivant leurs tailles
    for ligne in fichier:
        if (len(ligne)<=6):
            i+=1
            liste_debutant.append(ligne)

        if (len(ligne)>6 and len(ligne)<=9):
            i+=1
            liste_intermediaire.append(ligne)

        if (len(ligne)>9 ):
            i+=1
            liste_experimente.append(ligne)
    niveau1 = choix_niveau()
    if niveau1 == 1 :
        print("Vous avez choisi le niveau débutant")
        return liste_debutant
    elif niveau1 == 2:
        print("Vous avez choisi le niveau Intermediaire")
        return liste_intermediaire
    elif niveau1 == 3:
        print("Vous avez choisi le niveau Experiementé")
        return liste_experimente

    fichier.close()
#Presentation,choix et controle de saisi pour les niveaux
def choix_niveau():
    niveau = int(input("Entrez le chiffre correspondant pour choisir un niveau:\n1:Débutant \n2:Intermediaire\n3:Experimenté \nVotre choix : "))
    while niveau<1 or niveau>3:
        niveau = int(input("Niveau Innexistant relisez l'entete SVP" ))
    return niveau
#Tirage du mot dans la liste suivant le niveau du jeu
def tirage_mot(liste):
    return random.choice(liste)
#controle du saisi pour ne prendre que des lettre de l'alphabet et un caratere seulement
def saisie():
    lettre = input("Saisissez une lettre : ")
    while lettre.isalpha==False and len(lettre)>1:
        if lettre.isalpha()==False:
            print("Veuillez entrer une lettre de l'alphabet")
        if len()>1:
            print("Veuillez entrer un de charactere")
        lettre = input("Saisissez une lettre")
    return 

#verifie la presenece du lettre dans les mot a deviner et le mot haché
def verif(lettre,mot_secret,mot_devine):
        if presence(lettre,mot_secret)==presence(lettre,mot_devine):
            return True
        else : return False

#retourne le nombre d'ocurrence d'une lettre dans le mot
def presence(lettre,mot):
    return  mot.count(lettre)
#retourne dans une liste les indices d'une lettre dans le mot
def nbr_present(lettre,mot):
    liste=[]
    for i in range(len(mot)):
        if mot[i]==lettre:
            liste.append(i)
   
    return liste
    

#Construit le mot haché
def mot_test(mot_secret):
    taille =len(mot_secret)-1
    mot="_"
    for i in range(taille-1):
        mot=mot+"_"
    return mot
#effectue la substitution de la lettre dans le mot haché afin de guider le joueur
def remplacement(mot_test,mot_secret,lettre):
    nbr = nbr_present(lettre,mot_secret)
    mot_test = list(mot_test)
    if nbr != 0:
        for i in nbr:
            mot_test[i]=lettre
    mot_test = "".join(mot_test)
    return str(mot_test)
#retourne la liste des lettre pouvant etre utilisé pour determiner le mot
def lettres_restantes(lettre,alphabet):
    if alphabet.count(lettre)!=0:
        alphabet.remove(lettre)
    return alphabet
#Verifie si la lettre saisi est une voyelle ou une consonne
def erreur(a):
    consonne ="bcdfghjklmnpqrstvwxyz"
    if consonne.find(a)==-1:
        return 2
    else:
        return 1
#calcule le nombre de lettre unique dans le mot
def lettre_unique(mot):
    n=0
    for i in mot:
        if mot.count(i)==1:
            n+=1
    return n-1

#calcul le score obtenu par le joueur
def score(lettre_unique,tentative_restante):
    return lettre_unique*tentative_restante

#Progamme Principale

#Initialisation des parametres du jeu 
nbr_partie=0
partie = 0
best_score =0
point_erreur = 3
tentative =6
rejouer ="Y"
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet2=alphabet.copy()
#Debut du bloc gerant la partie : le menu principal 
#b est le mot haché
liste_mot=chargement()
while(rejouer=="Y" or rejouer=="y"):
    
    mot = tirage_mot(liste_mot)
    alphabet=alphabet2.copy()
    print(f"Vous devez deviner un mot de {len(mot)-1} lettre  {mot}")
    b=mot_test(mot)
   
    i=1
    o=len(mot)
#Controle et traiment des entrées 
    while i<o and tentative>0:
        print(f"Le nombre de tentative restante est de : {tentative}")
        text = "".join(alphabet)
        print(f"Lettre a utiliser : {text}")

        lettre = input("Saisissez une lettre :")
        while (lettre.isalpha()==False and tentative>0 ) or (len(lettre)>1 and tentative>0)   :
            if point_erreur>0:
                    point_erreur-=1
                    print(f"Erreur!!! Il vous reste {point_erreur} avertissements")
            if point_erreur==0:
                print("Vous perdez une tentative")
                tentative-=1
                print(f"Il vous reste {tentative} tentatives")

            if lettre.isalpha()==False:
                print("Veuillez entrer une lettre de l'alphabet")

            if len(lettre)>1:
                print("Veuillez entrer un caractère")
            lettre = input("Saisissez une lettre :")

        alphabet=lettres_restantes(lettre,alphabet)
#verification et remplacement de la lettre dans le mot haché
        if presence(lettre,mot)!=0 and lettre.isalpha()==True:
            if(verif(lettre,mot,b)):
                print("Lettre deja renseignée ")
            else:
                d=remplacement(b,mot,lettre)
                b=d
                i+=1
                if(presence(lettre,mot)>=2):
                    o=o-(presence(lettre,mot)-1)
            if(i==o):
                print("Vous avez gagné !!!")
                score_p=score(lettre_unique(mot),tentative)
                print(f"Votre score est de : {score_p}")
 #verification et notification dans le cas la lettre ne se trouve pas dans le mot               
        elif lettre.isalpha() : 
            print("Cette lettre n'est pas dans le mot")
            if erreur(lettre)==1:
                tentative -=1
            elif erreur(lettre)==2:
                tentative -=2
        if tentative==0 :
            print("Vous avez predu !!!")

#Info de fin de partie : score ,nombre de partie, proposition de rejouer
        print(b)    
    print(f"le mot caché était : {mot}")
    partie+=1
    if best_score<score_p:
        best_score=score_p
    if (partie>1):
        print(f"Votre meilleur score sur les {partie} parties jouées est de : {best_score}")
    rejouer = input("Appuyer sur Y pour rejouer autres touvhes pour quitter")  
  
print("Merci d'avoir joué . Bye Bye")   
       

