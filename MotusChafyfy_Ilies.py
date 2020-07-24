from tkinter import*
import sys
from random import *
import tkinter as tk
import programmeConsole


jeu = True

while jeu:

    y = 25
    canvas = None
    entre = None
    motComplete = []
    motBase = None
    positionLettresMalPlacees = []
    bienPlacee = []
    essaie = 0
    counter = 9
    mot=""
    erreur = []
    x0 = 0
    y0 = 50
    x1 = 50
    y1 = 100
    timer_id = None
    count = 8
    root = Tk()

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                    #----------------------RESTART---------------------------------#
    def recommencer():
        root150.destroy()

    def fin():
        root150.destroy()
        sys.exit(0)
    #--------------------------------------------------------------------------------------------------------#
    def restart_good():
        global root150
        #---------------------------------------------------------------------------------------------------#
        root.destroy()
        root150= Tk()
        
        root150.title("Bien Joué !")
        Victoire = tk.Label(root150,bg='green',text="VOUS AVEZ GAGNÉ EN", font=('Arial', '50'),fg='white')
        Victoire.grid(row=5,column=0)
        #---------------------------------------------------------------------------------------------------#
        textnbessai = Label(root150, text = str(essaie+1), font = "Arial 50" ).grid(row = 5, column = 4)
        print(textnbessai, end = '')
        textessai = Label(root150, text = 'ESSAI(S)', font = "Arial 50" ).grid(row = 5, column = 5)
        #---------------------------------------------------------------------------------------------------#
        Continuer = Button(root150,bg='white',text="RECOMMENCER ?", font=('Arial', '50'), command=recommencer)
        Continuer.grid(row=7,column=0)
        Stop = Button(root150,bg='white',text="ARRETER ?", font=('Arial', '50'), command=fin)
        Stop.grid(row=20,column=0)
        root150.mainloop()



#----------------------------------------------------------------------------------------
    def restart_bad():
        #---------------------------------------------------------------------------------------------------#
        root.destroy()
        root150= Tk()
    
        root150.title("C'est perdu !")

        Defaite = tk.Label(root150,bg='red',text="GAME OVER", font=('Arial', '50'),fg='white')
        Defaite.grid(row=5,column=0)
        Continuer = Button(root150,bg='white',text="CONTINUER ?", font=('Arial', '50'), command=recommencer)
        Continuer.grid(row=7,column=0)
        Stop = Button(root150,bg='white',text="ARRETER ?", font=('Arial', '50'), command=fin)
        Stop.grid(row=20,column=0)
        #----------------------------------------------------------------------------------------------------------------#
        textlose = Label(root150, text = 'Vous avez perdu.. donc voici le mot : ', bg = "red",fg = "white",font = "Arial 25" ).grid(row = 1, column = 0)
        print(textlose)
        bonmot = Label(root150, text = motBase, bg = "red",fg = "white",font = "Arial 25" ).grid(row = 1, column =3)
        print(bonmot)
        root150.mainloop()

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
    def quitter():
        root.destroy()
        sys.exit(0)
    quitter = Button(root, text="QUITTER", command=quitter)
    quitter.grid(column=4)
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                    #----------------------Chronomètre---------------------------------#

    def start_timer():
        global timer_id, count

        if count > 0:
            label ['text'] = count
            count -= 1
            timer_id = root.after(1000, start_timer)
        else:
            rootchr = Tk()
            rootchr.title("FIN CHRONO")
            bouton = Button(rootchr, text="Ok", command=rootchr.destroy)
            bouton.grid()
            reset_timer()
            tempsfini = Label(rootchr, text="Le temps imparti est dépassé.. ", font=('Times', '18'),fg='red').grid()
            timer_id = None #Objet Vide


    def reset_timer():
        global timer_id, count
        if timer_id:
            root.after_cancel(timer_id)
            timer_id = None
        count = 8
        label ['text'] = count
            #--------------------------------------------------------#
    label = Label(root, text=count, bg = "coral1", fg = "white", font = "Arial 20")
    label.grid(column = 3 )
    Button(root, text='start', command=start_timer).grid(column = 3)


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                    #----------------------Bienvenue---------------------------------#

    def Bienvenue():
        root4 = Tk()
        root4.title("Bienvenue")
        frame = Frame(root4)
        frame.grid()
        button = Button(frame, text="| Rentrer dans le JEU |", command=root4.destroy)
        button.grid()
        label = Label(root4,text="Bienvenue sur le JEU MOTUS : Réalisé par Enzo - Ilies et Thomas",font=("Arial Black", 20)).grid()


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                    #----------------------Affichage mot Utilisateur --------------------------#
    def afficherMotChosis(mot):
        global y
        global canvas
        liste = programmeConsole.mini_en_Maj(mot)
        #print(liste)
        x = 25
        x0 = 0
        x1 = 50
        for loop in range(len(liste)):                              #Affichage
            rectangle = canvas.create_text( x,y,text=liste[loop],font=("Arial Black", 25), fill = 'white')
            x=x+50
        y = y + 50


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                    #----------------------Affichage mot Complete --------------------------#
    def afficherMotComplete(mot,motChoisi,x0,x1):
        global y
        global y0
        global y1
        global canvas
        global motComplete
        liste = programmeConsole.mini_en_Maj(mot)
        #print(liste)
        x = 25
        for loop in range(len(liste)):                                   #Mot bien placé et mal placé + MotComplete
            if liste[loop] == motChoisi[loop]:
                rectangle = canvas.create_rectangle(x0, y0, x1, y1, fill = "red")
                canvas.tag_lower(rectangle)
                motComplete[loop] = motChoisi[loop]
            elif liste[loop] in motChoisi:
                cercle = canvas.create_oval(x0+1, y0+1, x1-2, y1-2,fill = "gold")
                canvas.tag_lower(cercle)
            x0 = x0 + 50
            x1 = x1 + 50
        y0 = y0 + 100
        y1 = y1 + 100

        for loop in range(len(motComplete)):                              #Affichage
            canvas.create_text( x,y,text=motComplete[loop],font=("Arial Black", 25),fill = 'white',)
            reset_timer()
            start_timer()
            x=x+50
        y = y + 50

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                    #----------------------INTERFACE --------------------------#
    def creationInterface(nbLettre,motChoisi):
        #-----------------------------Initialisation------------------------------------#
        global canvas
        global entre
        global motBase
        #-------------------------------------------------------------------------------#
        root.title("MOTUS")
        root.configure(background = 'coral1')
        #-------------------------------------------------------------------------------#

                        #----------"MOTUS" AFFICHAGE----------------#
        label_one = Label(root, text = '|MOTUS|',font=("Arial", 40), fg = "white",bg = "coral1" )
        label_one.grid(row = 0)

        #-------------------------------------------------------------------------------#
                        #----------Label Veuillez entrer un mot---------#
        Label(root, text = "Veuillez entrer un mot", bg="cyan",fg="tomato",font="none 12 bold").grid(row=1,column=0)

        #-------------------------------------------------------------------------------#
                        #----------------Boite d'entrée---------------#
        entre = Entry(root)
        entre.grid(row=2,column=0)

        #-------------------------------------------------------------------------------#
                        #--------------Creation des lignes--------------#
        y = 25
        canvas_width = nbLettre * 50
        canvas_height = 600
        canvas = Canvas(root, width=canvas_width,height=canvas_height, bg="deep sky blue")

        x0,y0,x1,y1= 0,0,nbLettre*50,0 #Lignes
        for loop in range(12):
            canvas.create_line(x0,y0,x1,y1,width = 2, fill="white")
            y0= y0 + 50
            y1= y1 + 50

        x0,y0,x1,y1= 0,0,0,nbLettre*100  #Colonnes
        for loop in range(nbLettre+1):
            canvas.create_line(x0,y0,x1,y1,width = 2,fill="white")
            #476042
            x0= x0 + 50
            x1= x1 + 50
        canvas.grid(row =5)

        #-------------------------------------------------------------------------------#
                            #----------------Bouton---------------#
        bouton = Button(root, text="ENTREE", command=boutonClic)
        bouton.grid(row=3,column=0)

        #----------------------Mot Complete Initialisation------------------------------#

        motComplete.append(motChoisi[0])
        erreur.append(".")
        for loop in range (len(motChoisi) - 1):
            motComplete.append(".")
            erreur.append(".")
        afficherMotChosis(motComplete)
        motBase = list(motChoisi)
        root.mainloop()
        return canvas

    #--------------------------------------------------------------#
    def boutonClic():
        global essaie
        mot = entre.get()
        if  mot.isalpha() == True:
            mot = str(mot)
            mot = list(mot)
            mot = programmeConsole.mini_en_Maj(mot)
            if motBase != mot and essaie < 6:
                if len(mot) == len(motBase):
                    if programmeConsole.validiteMot(mot) == False :
                        #------------------------------------------#
                        root7 = Tk()
                        frame = Frame(root7, bg ="white")
                        button = Button(frame)
                        button['text'] ="| Ok |"
                        button['command'] = root7.destroy
                        root7.title("! Langue !")
                        fautelangue = Label(root7, text="Ecrire un mot qui existe dans la langue Française, Merci !", font=('Times', '18'),fg='red').grid()
                        frame.grid()
                        button.grid()
                        #------------------------------------------#
                        #------------------------------------------#
                    else:
                        afficherMotChosis(mot)
                        afficherMotComplete(mot,motBase,x0,x1)
                        entre.delete(0, 'end')
                        essaie = essaie + 1
                else:
                    mot = erreur
                    afficherMotChosis(mot)
                    afficherMotComplete(mot,motBase,x0,x1)
                    #------------------------------------------#
                    #------------------------------------------#
                    root5 = Tk()
                    root5.title("Oupsss..")
                    frame = Frame(root5)
                    button = Button(frame)
                    button['text'] ="| Ok |"
                    button['command'] = root5.destroy
                    label = tk.Label(root5, text="Ton mot n'est pas de bonne longueur, tu as perdu un essaie", font=('Times', '18')).grid()
                    reset_timer()
                    frame.grid()
                    button.grid()
                    #------------------------------------------#
                    #------------------------------------------#
                    essaie = essaie +1

            elif motBase == mot and essaie < 6:
                #------------------------------------------#
                restart_good()

                #------------------------------------------#
            elif motBase != mot and essaie == 6:
                #------------------------------------------#
                reset_timer()
                restart_bad()


        #----------------------------------------------------#
        else:
            root2 = Tk()
            frame = Frame(root2)
            button = Button(frame)
            button['text'] ="| Ok |"
            button['command'] = root2.destroy
            root2.title("Erreur")
            label = tk.Label(root2, text='Ne rentrez que des lettres !', font=('Times', '18'),fg='red').grid()
            frame.grid()
            button.grid()
            #------------------------------------------#
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
               #---------------MAIN----------------------# 
    def main():
        global canvas
        motChoisi = programmeConsole.choixDuMot()
        canvas = creationInterface(len(motChoisi),motChoisi)


    Bienvenue() #Renvoie une fenetre de bienvenue
    main() #Lancement du Jeu

