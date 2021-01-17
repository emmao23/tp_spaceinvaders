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
Mafenetre.title("Space invaders")
 
#Création d'un Canvas dans Mafenetre.
ZoneGraph = tk.Canvas(Mafenetre, height=1300, width=1000)

#Lien images
iFond=tk.PhotoImage(file="../Images/fond1.png") 
iVaisseau=tk.PhotoImage(file="../Images/vaisseau.png")
iLaserRouge=tk.PhotoImage(file="../Images/laserbleu.gif")
iLaserBlue=tk.PhotoImage(file="../Images/laserrouge.gif")

ImFond=ZoneGraph.create_image(20,40, anchor=tk.NW,image=iFond)

#Creation du menu
MenuBar = tk.Menu(Mafenetre)
MenuNiveau = tk.Menu(MenuBar,tearoff=0)
MenuNiveau.add_command(label="Niveau 3 : tir rapide", command=FT.Niveau3)
MenuNiveau.add_command(label="Niveau 2: tir moins rapide", command=FT.Niveau2)
MenuNiveau.add_command(label="Niveau 1 :tir lent", command=FT.Niveau1)
MenuBar.add_cascade(label="Niveau",menu=MenuNiveau)
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
Ts1 = ZoneGraph.create_text(10,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Score :" )
FT.Affiche(ZoneGraph)


Tv1 = ZoneGraph.create_text(600,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Vie :" )
 
Frame1=tk.Frame(Mafenetre)
Frame1.pack(side=tk.RIGHT)

Debut=tk.Button(Frame1,text="Nouvelle partie",command=lambda:FT.Rejouer(Mafenetre,ZoneGraph))
Debut.pack(side = tk.RIGHT, padx = 5)

Fin=tk.Button(Frame1,text="Quitter", command=lambda:FT.Quitter(Mafenetre))
Fin.pack(side = tk.BOTTOM, padx = 5)


#On place le Canvas ZoneGraphique sur la fenètre
ZoneGraph.pack()


PosX=300
PosY=300 
L=[]
LTir=[]
LDarky=[]
temps=time.time()
Labris=[]
Fin=False
Vaisseau=0

FT.CreationVaisseau(ZoneGraph,iVaisseau)
FT.CreationAliens(Mafenetre,ZoneGraph,PosX,PosY)
FT.Deplacement(Mafenetre,ZoneGraph,2)
FT.TirAlien(ZoneGraph,Mafenetre) 
FT.CreationEnnemiBonus(ZoneGraph,Mafenetre)
FT.CreationAbri(ZoneGraph,PosX,650)
FT.ConditionFin(Mafenetre,ZoneGraph)
#  On met le focus sur le canvas
ZoneGraph.focus_set()

ZoneGraph.bind("<Key>",lambda event:FT.ToucheClavier(Mafenetre,ZoneGraph,iLaserRouge,event))

#On utilise mainloop pour que la fenetre soit active tout le temps
Mafenetre.mainloop()



