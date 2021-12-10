from colorama import Back, Fore, Style, deinit, init # importation de coloroma permettant changement couleur de texte
import random               #importation de l'aleatoire

init() #demarage colorama
#************Fonction Principale permettant la verif du mot entré par le joueur***************
def verifPresence(motrdm,imotentry,motentry):
    for i in range(len(motrdm)):
        if motentry[imotentry]==motrdm[i]:      #verifie si la lettre est dans le mot
            if imotentry==i:                        #verifie si lettre est au meme emplacement
                print( Fore.RED+ motentry[imotentry],end='')        #si oui ---> rouge
                imotentry=imotentry+1    #i du mot +1
            else:
                print( Fore.YELLOW+ motentry[imotentry],end='')     #si present mais pas mm place ----> jaune
                imotentry=imotentry+1    #i du mot +1
    return False            #si pas present retourne Faux
#**********************************************************************************************
#**************Init Des val utiliser************************
dico={1:'accent', 2:'aduler', 3:'helico', 4:'boxeur', 5:'surimi', 6:'tajine', 7:'serrer', 8:'defend', 9:'emojis', 10:'espece'} #creation d'un dico contenant 10 mot de 6 lettres
motiallée= random.randint(1,10)
motrdm=dico[motiallée]
imotentry=0
tentative=0
#*********************************************************
#******************Boucle Principale du jeu****************************************************
while tentative!=8:                                              #Verifie en tout premier si les tentatives ne depasse pas le max
    motentry=(input("entrer un mot de 6 lettres:"))  #entrée du mot par le joueur
    if motentry==motrdm:                #verifie en priorité si le joueur a le bon mot
        print("Vous avez gagné !")          #affichage si reussite
        quit()              #fin du programme
    else:
        for i in range (len(motrdm)):       #durant la longueur du mot:
            if verifPresence(motrdm,imotentry,motentry)==False:     #si lettre pas trouvé
                print(Fore.BLUE + motentry[imotentry],end='')   #lettre non presente ----> bleue
                imotentry=imotentry+1               #i du mot +1
        tentative=tentative+1                #ajoute +1 au tentaive
        imotentry=0       #i du mot =0 car nouveau mot
print(" Perdu ! Le mot etait :" + motrdm)    #affichage en cas de defaite
#***********************************************************************************************
deinit() #fin colorama

#bug 1: si la lettre trouvé est la derniere lettre il n'y a pas de reset d'imotentry ----> out of index string
#bug 2: refait deux fois la meme lettre quand elle est bonne.
#solution: reussir a faire en sorte que la fonction s'arrete quand lettre bonne trouvé sans que le imotentry soit perturber
