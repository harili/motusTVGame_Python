from random import *

                                                   #Fichier des fonctions du programme sur console utile sur l'affichage.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def mini_en_Maj(motUtilisateur):
    #Met la liste en majuscule quelque soit l'orthograpphe du mot: (ex: MaNgEr --> MANGER / ['M','a','N','g','E','r'] --> ['M','A','N','G','E','R'])
    liste = motUtilisateur
    liste = "".join(liste)
    liste = liste.upper()
    liste = list(liste)
    return liste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#




#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def verifPourChoixMot(informationEntree):
    while informationEntree.isdigit() == False :
        informationEntree = input("Ne rentrez que des chiffres entre 6 et 10 SVP.")
    return informationEntree

def choixDuMot():
    informationEntree = input("Longueur du mot entre 6 et 10 lettres")
    informationEntree = verifPourChoixMot(informationEntree)
    L = int(informationEntree)
    while (L < 6 or L > 10 ):
        informationEntree = input("Longueur du mot entre 6 et 10 lettres")
        informationEntree = verifPourChoixMot(informationEntree)
        L = int(informationEntree)


                         #ouvrir le bon fichier avec des mots de bonne longueur

    if L == 6:
        fichier = open('Mots6.txt','r')
        list1 = fichier.readline()
    elif L== 7:
        fichier = open('Mots7.txt','r')
        list1 = fichier.readline()
    elif L == 8:
        fichier = open('Mots8.txt','r')
        list1 = fichier.readline()
    elif L == 9:
        fichier = open('Mots9.txt','r')
        list1 = fichier.readline()
    elif L == 10:
        fichier = open('Mots10.txt','r')
        list1 = fichier.readline()

                        #Enlever les accents dans la liste #Séparer les mots de la liste + majuscules #Sélection aléatoire de mots dans la liste

    if L>=6 and L<=10:
        accent = ['é', 'è', 'ê', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', 'à']
        sans_accent = ['e', 'e', 'e', 'u', 'u', 'c', 'o', 'i', 'i', 'a', 'a']

        for i in range(len(accent)):
            list1 = list1.replace(accent[i], sans_accent[i])

        list_mots = list1.upper()
        list_mots = list_mots.split(", ")

    motIni = choice(list_mots)
    print(motIni)
    fichier.close()
    return motIni

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#




#--------------------------------------------------------------------------------------------------------------------------------------------------------------#

def validiteMot(demandeMot):
    if len(demandeMot) == 6:
        fichier = open('MotsComplets6.txt','r')
        dico = fichier.readline()
    elif len(demandeMot)== 7:
        fichier = open('MotsComplets7.txt','r')
        dico = fichier.readline()
    elif len(demandeMot) == 8:
        fichier = open('MotsComplets8.txt','r')
        dico = fichier.readline()
    elif len(demandeMot) == 9:
        fichier = open('MotsComplets9.txt','r')
        dico = fichier.readline()
    elif len(demandeMot) == 10:
        fichier = open('MotsComplets10.txt','r')
        dico = fichier.readline()

    demandeMot = "".join(demandeMot)
    dico = dico.split(", ")
    if demandeMot in dico:
        return True
    else:
        return False
    fichier.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#