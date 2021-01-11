# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:17:44 2021

@author: emma
"""

import tkinter as tk
import random as Rd
import time 
from tkinter import messagebox
import fonctions as FT


#Création de la fenêtre principale.
Mafenetre = tk.Tk()

#On modifie le titre de la fenètre
Mafenetre.title("Space invader la chute de l'étoile noire")
 
#Création d'un Canvas (zone graphique) dans Mafenetre.
ZoneGraphique = tk.Canvas(Mafenetre, height=1300, width=1000)

#Lien images
iFond=tk.PhotoImage(file="../Images/fond1.png") 
iVaisseau=tk.PhotoImage(file="../Images/xwing.png")
iLaserRouge=tk.PhotoImage(file="../Images/pioupioubleu.gif")
iLaserBlue=tk.PhotoImage(file="../Images/pioupiourouge.gif")

ImFond=ZoneGraphique.create_image(10,40, anchor=tk.NW,image=iFond)

#Creation du menu
MenuBar = tk.Menu(Mafenetre)
MenuMode = tk.Menu(MenuBar,tearoff=0)
MenuMode.add_command(label="Mode simple : tir rapide", command=FT.Mode1)
MenuMode.add_command(label="Mode Normal: tir moins rapide", command=FT.Mode2)
MenuMode.add_command(label="Mode Difficile :tir lent", command=FT.Mode3)
MenuBar.add_cascade(label="Mode",menu=MenuMode)
MenuAide = tk.Menu(MenuBar,tearoff=0)
MenuAide.add_command(label="Règle du jeu",command=FT.Regle)
MenuBar.add_cascade(label="Aide",menu=MenuAide)
MenuScore = tk.Menu(MenuBar,tearoff=0) 
MenuScore.add_command(label="Afficher les scores",command=FT.Afficher)
MenuScore.add_command(label="Réinitialiser les scores",command=FT.Reinitialiser)
MenuBar.add_cascade(label="Score",menu=MenuScore)
Mafenetre.config(menu=MenuBar)

Vie=3
Score=0

#On ajoute des zones de texte sue le canvas
Ts1 = ZoneGraphique.create_text(10,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Score :" )
FT.Affiche(ZoneGraphique)


Tv1 = ZoneGraphique.create_text(600,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Vie :" )
 
Frame1=tk.Frame(Mafenetre)
Frame1.pack(side=tk.RIGHT)

Debut=tk.Button(Frame1,text="Nouvelle partie",command=lambda:FT.Rejouer(Mafenetre,ZoneGraphique))
Debut.pack(side = tk.RIGHT, padx = 5)

Fin=tk.Button(Frame1,text="Quitter", command=lambda:FT.Quitter(Mafenetre))
Fin.pack(side = tk.BOTTOM, padx = 5)


#On place le Canvas ZoneGraphique sur la fenètre
ZoneGraphique.pack()


PosX=300
PosY=300 
L=[]
LTir=[]
LDarky=[]
temps=time.time()
Labris=[]
Fin=False
Vaisseau=0

FT.CreationVaisseau(ZoneGraphique,iVaisseau)
FT.CreationAliens(Mafenetre,ZoneGraphique,PosX,PosY)
FT.Deplacement(Mafenetre,ZoneGraphique,2)
FT.TirAlien(ZoneGraphique,Mafenetre) 
FT.CreationEnnemiBonus(ZoneGraphique,Mafenetre)
FT.creation_abri(ZoneGraphique,PosX,650)
FT.ConditionFin(Mafenetre,ZoneGraphique)
#  On met le focus sur le canvas
ZoneGraphique.focus_set()

ZoneGraphique.bind("<Key>",lambda event:FT.ToucheClavier(Mafenetre,ZoneGraphique,iLaserRouge,event))

#On utilise mainloop pour que la fenetre soit active tout le temps
Mafenetre.mainloop()



