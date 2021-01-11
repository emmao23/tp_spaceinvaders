# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:38:46 2021

@author: emma
"""
import tkinter as tk
import random as Rd
import time 
from tkinter import messagebox


LDarky=[]
temps=time.time()
Labris=[]
LTir=[]
L=[]
Score=0
Ts2=0
Txt="Détruis l'étoile noire, que la force soit avec toi!\n\nFleches gauche-droite pour se déplacer\nEspace pour tirer"
cadence=2
Fin=False
Vaisseau=0
iFond=0
Tv2=0


def Mode1():
    global cadence
    cadence = 0.5


def Mode2():
    global cadence
    cadence = 2


def Mode3():
    global cadence
    cadence = 4


def Quitter(Mafenetre):
     Mafenetre.destroy()


def Regle():
    messagebox.showinfo("Règles du jeu",Txt)
    
    
  
def Reinitialiser():
    FichierS = open("../Fichiers/Score.txt",'w')
    FichierS.close
    messagebox.showinfo("Réinitialisation","Remise des scores à 0")
    
    
def Afficher():
    FichierS = open("../Fichiers/Score.txt",'r')
    Scores = FichierS.read()  
    FichierS.close
    messagebox.showinfo("Scores:","Les scores sont :\n"+Scores)


##############################################################################fonction action


def Deplacement(Mafenetre,ZoneGraphique,Dx):
    global L,Fin,Vaisseau
    
    Dy = 0
  
    for i in L:
        if len(i)!=0:
            if i[-1].x>850:
                Dx=-Dx
                break
            if i[0].x<30:
                Dx=-Dx
                Dy = 10
                break
            

    for i in L:
        for j in i:
            ZoneGraphique.move(j.objet,Dx,Dy)
            j.x+=Dx
            j.y+=Dy
         
  
    if Fin == False:
        Mafenetre.after(100,lambda:Deplacement(Mafenetre,ZoneGraphique,Dx))  


def ToucheClavier(Mafenetre,ZoneGraphique,i6,event):
    global temps,Labris,L,cadence,Vaisseau
    
    touche = event.keysym  
    Pas = 0
    if touche == 'Right':  
        if Vaisseau.x < 850:  
            Pas = 10 
            Vaisseau.x += Pas
    if touche == 'Left':  
        if Vaisseau.x > 30:   
            Pas =- 10
            Vaisseau.x += Pas            
    if touche == 'space':
        T=time.time()
        if T-temps>cadence:
            temps=T
            obj=CreationTir(ZoneGraphique,Vaisseau.x,i6)
            MouvTir(Mafenetre,ZoneGraphique,obj)
            del obj
        
    ZoneGraphique.move(Vaisseau.objet,Pas,0)  


def TirAlien(ZoneGraphique,Mafenetre):
    global Labris, LTir, L, Fin, Vaisseau
    
    i7=tk.PhotoImage(file="../Images/pioupiourouge.gif")    
    
    CreationTirsAlien(ZoneGraphique,i7)     
    MouvTirAlien(Mafenetre,ZoneGraphique)
    
    if Fin == False:
        Mafenetre.after(50,lambda:TirAlien(ZoneGraphique,Mafenetre))


def MouvTirAlien(Mafenetre,ZoneGraphique):
    global Labris,LTir, Vaisseau
    
    Action=False

    for i in LTir:
        for j in range(len(Labris)):
            try :
                k=LTir.index(i)
                Explos = LTir[k].mur(Mafenetre,ZoneGraphique,Labris[j])
                if Explos == True:
                    del Labris[j]
                    del LTir[k]
                    MouvTirAlien(Mafenetre,ZoneGraphique)            
            except ValueError:
                return
   
    for i in range(len(LTir)):
        T,Tv2 = LTir[i].attaque(Mafenetre,ZoneGraphique)
        if T == True :
            del LTir[i]
            Action=True
            break
                    
     
    for i in range(len(LTir)):     
        Destr = LTir[i].destruction(ZoneGraphique)
        if Destr == True:
            del LTir[i]
            Action=True
            break
    
    
    if Action == True :
        MouvTirAlien(Mafenetre,ZoneGraphique)        
   
     
    for i in LTir:
        ZoneGraphique.move(i.objet,0,+10)
        i.y+=10
    return 


def DeplacementEnnemiBonus(ZoneGraphique,Mafenetre):

    
    for i in LDarky:
        ZoneGraphique.move(i.objet,10,0)
        i.x+=10
        
        
def MouvTir(Mafenetre,ZoneGraphique,obj):
    global Labris,L ,Fin   
    
  
    for i in range(len(Labris)):
        Explos = obj.mur(Mafenetre,ZoneGraphique,Labris[i])
        if Explos == True:
            del Labris[i]
            return
        

    for i in range(len(L)):
        for j in range(len(L[i])):
            Explos = obj.explosion(ZoneGraphique,L[i][j])
            if Explos == True:
                del L[i][j]
                return 
                

    for i in range(len(LDarky)):
        Explos = obj.explosion(ZoneGraphique,LDarky[i])
        if Explos == True:
            del LDarky[i]
            return 
        
 
    Destr = obj.destruction(ZoneGraphique)
    if  Destr == False:
        ZoneGraphique.move(obj.objet,0,-10)
        obj.y-=10
        if Fin == False:
            Mafenetre.after(50,lambda:MouvTir(Mafenetre,ZoneGraphique,obj))
    else :
        return        
  
##########Fonctions Creation##########

      
      

def CreationEnnemiBonus(ZoneGraphique,Mafenetre):
    global LDarky,Fin
    
    iDarky=tk.PhotoImage(file="../Images/supermechant.png")
    Rand = Rd.randint(0, 99) 
    if Rand == 0:
        Image=ZoneGraphique.create_image(-100,50,anchor=tk.NW,image=iDarky)         
        Darky=Elements(Image,-100,50,iDarky,1,150)
        LDarky.append(Darky)
        
    DeplacementEnnemiBonus(ZoneGraphique,Mafenetre)
    
    if Fin == False:
        Mafenetre.after(100,lambda:CreationEnnemiBonus(ZoneGraphique,Mafenetre))


def CreationTirsAlien(ZoneGraphique,i7):

    global LTir,L
    L2=[]    
    for i in L:
        if len(i)!=0:
            L2.append(i)
            
    Rand = Rd.randint(0, 99) 
    if Rand <= 3:
        Ligne = Rd.randint(0,len(L2)-1)
        Colonne = Rd.randint(0,len(L2[Ligne])-1)
        LTir.append(CreationTirAlien(ZoneGraphique,L[Ligne][Colonne],i7))
        
    elif Rand <= 5:
        for i in [1,1]:
            Ligne = Rd.randint(0,len(L2)-1)
            Colonne = Rd.randint(0,len(L2[Ligne])-1)
            LTir.append(CreationTirAlien(ZoneGraphique,L[Ligne][Colonne],i7))
      
    
def CreationTirAlien(ZoneGraphique,Alien,i7):

    
    PosX=Alien.x + 50   
    PosY=Alien.y + 50
    Laser=ZoneGraphique.create_image(PosX,PosY,image=i7)
    obj = Elements(Laser,PosX,PosY,i7,1,0)
    return obj
 

def CreationTir(ZoneGraphique,PosX,i6):
  
    time
    PosY=680
    Laser=ZoneGraphique.create_image(PosX+50,PosY,image=i6)
    obj = Elements(Laser,PosX+50,PosY,i6,1,0)
    return obj


def CreationAlien(Mafenetre,ZoneGraphique,Nom,PosY,im,Li,Score):
  
    
    PosX=int(Nom[1:])
    Image=ZoneGraphique.create_image(PosX,PosY,anchor=tk.NW,image=im)         
    Nom='Image'+Nom
    Nom=Elements(Image,PosX,PosY,im,1,Score)
    Li.append(Nom)
    return Li


def CreationAliens(Mafenetre,ZoneGraphique,PosX,PosY):
  
    global L    
    

    iYoda=tk.PhotoImage(file="../Images/mechant1.png")
    iBb8=tk.PhotoImage(file="../Images/mechant2.png")
    
    #Création de la liste L qui se compose de 4 sous liste L1,L2,L3,L4
    for i in [['a100','a200','a300','a400','a500','a600','a700','a800'],['b100','b200','b300','b400','b500','b600','b700','b800'],['c100','c200','c300','c400','c500','c600','c700','c800'],['d100','d200','d300','d400','d500','d600','d700','d800']]:
        if i==['a100','a200','a300','a400','a500','a600','a700','a800']:
            L1=[]
            for j in i:
                L1=CreationAlien(Mafenetre,ZoneGraphique,j,100,iBb8,L1,25)
            L.append(L1)
        if i==['b100','b200','b300','b400','b500','b600','b700','b800']:
            L2=[]
            for j in i:
                L2=CreationAlien(Mafenetre,ZoneGraphique,j,150,iBb8,L2,25)
            L.append(L2)
        if i==['c100','c200','c300','c400','c500','c600','c700','c800']:
            L3=[]
            for j in i:
                L3=CreationAlien(Mafenetre,ZoneGraphique,j,200,iYoda,L3,10)
            L.append(L3)
        if i==['d100','d200','d300','d400','d500','d600','d700','d800']:
            L4=[]
            for j in i:
                L4=CreationAlien(Mafenetre,ZoneGraphique,j,250,iYoda,L4,10)
            L.append(L4)
    
  
def CreationVaisseau(ZoneGraphique,iVaisseau):

    global Vaisseau    
    
    Px=300
    Py=680
    ImVaisseau=ZoneGraphique.create_image(Px,Py,anchor=tk.NW,image=iVaisseau)        
    Vaisseau=Elements(ImVaisseau,Px,Py,iVaisseau,3,0)
    
    

def creation_abri(ZoneGraphique,Dx,Dy):

    global Labris
    
    for i in range(4):
        for j in range(5):
            abri=ZoneGraphique.create_rectangle(Dx+j*30,Dy-20*i,Dx+30+j*30,Dy+20-i*20, fill='gray')
            abr=Elements(abri,Dx+j*30,Dy-20*i,'rect',1,0)            
            Labris.append(abr)

##########Fonctions Conditions et Fin de partie##########

            
def NewGame(Mafenetre,ZoneGraphique):

    global Score,L,LTir,LDarky,temps,Fin,Vaisseau,Labris,Tv2,iFond
    
    Score=0
    iVaisseau=tk.PhotoImage(file="../Images/xwing.png")
    
    iFond=tk.PhotoImage(file="../Images/fond1.png") 
    ImFond=ZoneGraphique.create_image(10,40, anchor=tk.NW,image=iFond)

  
    Ts1 = ZoneGraphique.create_text(10,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Score :" )
    Affiche(ZoneGraphique)
    

    Tv1 = ZoneGraphique.create_text(600,10, anchor=tk.NW, font=('Times', -18, 'bold'), text="Vie :" )   
    
    PosX=300
    PosY=300 
    L=[]
    LTir=[]
    LDarky=[]
    temps=time.time()
    Labris=[]
    Fin=False
    
    CreationVaisseau(ZoneGraphique,iVaisseau)
    CreationAliens(Mafenetre,ZoneGraphique,PosX,PosY)
    Deplacement(Mafenetre,ZoneGraphique,5)
    TirAlien(ZoneGraphique,Mafenetre) 
    CreationEnnemiBonus(ZoneGraphique,Mafenetre)
    creation_abri(ZoneGraphique,PosX,650)
    ConditionFin(Mafenetre,ZoneGraphique)
    
    
        
    
def Affiche(ZoneGraphique,Vie=3):

    global Ts2, Tv2
     
    Ts2 = ZoneGraphique.create_text(120,10, anchor=tk.NW, font=('Times', -18, 'bold'), text=Score)
    Tv2 = ZoneGraphique.create_text(650,10, anchor=tk.NW, font=('Times', -18, 'bold'), text=Vie)  

def ScoreTotal():

    global Score    
    
    FichierS = open("../Fichiers/Score.txt",'a')
    FichierS.write(str(Score)+"\n")
    FichierS.close()


def Rejouer(Mafenetre,ZoneGraphique,Message='Rejouer'):

    global Fin    
    
    Fin=True
    Msg = messagebox.askquestion(Message,"Voulez vous rejouer ?")
    if Msg == "yes":
        Remisea0(Mafenetre,ZoneGraphique)
        NewGame(Mafenetre,ZoneGraphique)
    else:
        Mafenetre.destroy()
         

def Remisea0(Mafenetre,ZoneGraphique):

    
    ZoneGraphique.delete('all')
    

def ConditionFin(Mafenetre,ZoneGraphique):
  
    global L ,Fin, Vaisseau
    
    for i in L:
        for j in i:
            j.colision(ZoneGraphique)
    
    
    if Vaisseau.defaite()==True:
        Fin=True
        ZoneGraphique.delete(Vaisseau.objet)
        Rejouer(Mafenetre,ZoneGraphique,'Perdu')
        return
        
    cpt=0
    for i in L:
        cpt+=len(i)
    
    if cpt==0:
        Fin=True
        ScoreTotal()
        Rejouer(Mafenetre,ZoneGraphique,'Victoire')
        return
    
    if Fin == False:    
        Mafenetre.after(200,lambda:ConditionFin(Mafenetre,ZoneGraphique))  




##########Classe des Elements du Canvas##########



    
class Elements:

    
    def __init__(self, Objet, PosX, PosY, Categorie, Vie, Score):
        
        
        self.objet = Objet
        self.x = PosX
        self.y = PosY
        self.categorie = Categorie
        self.vie = Vie
        self.score = Score
      
      
    def destruction(self,ZoneGraphique):

        
        if self.y<50:
            ZoneGraphique.delete(self.objet)
            return True
        if self.y>730:
            ZoneGraphique.delete(self.objet)
            return True
        return False                        
          
          
    def explosion(self,ZoneGraphique, Alien):

        global Score,Ts2        
        
        if self.x -100 <= Alien.x <= self.x :
            if self.y - 50 <= Alien.y <= self.y:
                ZoneGraphique.delete(self.objet)
                ZoneGraphique.delete(Alien.objet)
                Score+=Alien.score
                ZoneGraphique.delete(Ts2)
                Ts2 = ZoneGraphique.create_text(120,10, anchor=tk.NW, font=('Times', -18, 'bold'), text=Score)
                return True
        return False
    
    
    def defaite(self):


        if self.vie==0:
             return True
        return False

             
    def colision(self,ZoneGraphique):

        global Vaisseau        
        
        if self.y + 50 > 680:
            ZoneGraphique.delete(self.objet)
            Vaisseau.vie=0
    
    
    def attaque(self,Mafenetre,ZoneGraphique):

        global Vaisseau,Tv2       
        
        if self.y > 680:
            if Vaisseau.x  <self.x < Vaisseau.x+100:
                Vaisseau.vie -= 1
                ZoneGraphique.delete(self.objet)
                ZoneGraphique.delete(Tv2)
                Tv2 = ZoneGraphique.create_text(650,10, anchor=tk.NW, font=('Times', -18, 'bold'), text=Vaisseau.vie)
                return True,Tv2
        return False,Tv2
    
    
    def mur(self,Mafenetre,ZoneGraphique,abris):
       
        
        if self.x -30 <= abris.x <= self.x :
            if self.y - 20 <= abris.y <= self.y:
                ZoneGraphique.delete(self.objet)
                ZoneGraphique.delete(abris.objet)
                return True
        return False        
